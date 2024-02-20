import SqlAlchemy
from sqlalchemy import column, integer, string, create_engine, declarative_base
from sqlalchemy.exc import NoFutherResultFound

base = declarative_base()

class TodoItem(base):
    __tablename__ = "todo_items"
    id = column(integer, primary_key=True)
    name = column(string(320), nullable=False)
    description = column(string(), nullable=True)
    completed = column(bool, default=False)