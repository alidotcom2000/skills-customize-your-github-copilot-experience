from fastapi import FastAPI

app = FastAPI(title="Sample API")

# In-memory data store
items = [
    {"id": 1, "name": "Sample Item", "description": "This is a starter item."}
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}


@app.get("/items")
def get_items():
    # Return all items
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # Return the item matching item_id
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}


@app.post("/items")
def create_item():
    # Add a new item to the list and return it
    pass


@app.put("/items/{item_id}")
def update_item(item_id: int):
    # Update an existing item and return it
    pass
