from fastapi import FastAPI
from sqlalchemy import sqla_engine
from sqlalchemy.models import TodoItem, base
from sqlalchemy.database import Session
from sqlalchemy.crud import get_todos, create_todo

app = FastAPI()

@app.get("/todos")
def read_todos():
    with Session() as session:
        return session.query(TodoItem).all()

@app.post("/todos")
def create_todo(todo: TodoItem):
    with Session() as session:
        session.add(todo)
        session.commit()
        return { "status": "success", "message": "Todo added" }
