from fastapi import FastAPI

app = FastAPI()

items = [
    {"id": 1, "name": "Ali", "age": 20},
    {"id": 2, "name": "Sara", "age": 22}
]

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return {"message": "Item deleted"}
    return {"error": "Item not found"}