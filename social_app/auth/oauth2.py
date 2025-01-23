from jose import JWTError, jwt
from fastapi import Depends, status, HTTPException
from datetime import datetime, timedelta
from ..core import JWTSettings
from ..schemas import  TokenData
from fastapi.security import OAuth2PasswordBearer

oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')
jwt_settings = JWTSettings()

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=jwt_settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, jwt_settings.SECRET_KEY, algorithm=jwt_settings.ALGORITHM)

    return encoded_jwt

def verify_access_token(token:str, credentials_exeption):
    try:
        payload = jwt.decode(token, jwt_settings.SECRET_KEY, algorithms=[jwt_settings.ALGORITHM])
        id: str = payload.get("user_id")
        
        if id is None:
            raise credentials_exeption
        token_data = TokenData(id=id)
    except JWTError:
        raise credentials_exeption 
    return token_data
    
def get_current_user(token: str = Depends(oauth2_schema)):
    credentials_exeption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unathorized user:(", headers={"WWW-Authentificate":"Bearer"})
    return  verify_access_token(token, credentials_exeption)
    
    

