from fastapi import FastAPI
from .controllers import post_router, user_router
from .auth import auth_router
from .models import Base
from .database import engine

Base.metadata.create_all(bind=engine)

social_app = FastAPI()

social_app.include_router(post_router)

social_app.include_router(user_router)

social_app.include_router(auth_router)

@social_app.get("/")
async def root():
    return {"data": "Hello World"}