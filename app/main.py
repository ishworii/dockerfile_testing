from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    status: str = "not_completed"
    author: str | None = None
    date: datetime | None = None


app = FastAPI()


@app.get("/")
def root():
    return "Hello, world!"


@app.get("/greet/{name}")
def greet(name: str):
    return {"response": f"Hello,{name}"}


@app.post("/todo")
def display_todo(todo: Todo):
    return {"data": todo}
