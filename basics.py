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
@app.get("/todos/")
def show():
    return todos
@app.get("/todos/{item_id}")
def show_id(item_id:int):
    for todo in todos:
        if item_id==todo["id"]:
            return todo
        
    return {"error":"item did not found"}
@app.post("/todos/")
def add(todo:Todo):
    new_todo={"id":len(todos)+1,**todo.model_dump()}
    todos.append(new_todo)
    return(new_todo)
@app.delete("/todos/{item_id}")

def remove(item_id: int):
    for todo in todos:
        if item_id == todo["id"]:
            todos.remove(todo)
            return {"done": "deleted permanently"}
    return {"not found": "item not found"}
            
