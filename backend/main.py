from fastapi import FastAPI, HTTPResponse
from pydantic import SqlAlchemy
from sqlalchemy .database import engine, Session
from sqlalchemy .models import TodoItem
from sqlalchemy .init_db import init_db 

app = FastAPI()

@app.get("/")
def read_todos():
    with Session(bind=engine) as session:
        return session.query(TodoItem).all()
