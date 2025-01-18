FROM python:3.10

WORKDIR /social_app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "social_app.main:social_app", "--host", "0.0.0.0", "--port", "8000", "--reload"]