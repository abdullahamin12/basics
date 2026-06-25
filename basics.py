from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class Todo(BaseModel):
    title:str
    done:bool=False
todos=[
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Practice CRUD", "done": True}
]
todo = Todo(title="Buy milk", done=False)
print( todo.model_dump() )




