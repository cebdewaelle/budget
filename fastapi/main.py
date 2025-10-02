from fastapi import FastAPI
import os
from sqlalchemy import create_engine

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)


@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}
