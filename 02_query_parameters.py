from typing import Union
from fastapi import FastAPI

# Query parameters example
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

app = FastAPI()

# Query parameters
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# Optional parameters
@app.get("/items/{item_id}")
async def red_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id" : item_id, "q" : q}
    return {"item_id": item_id}

# Query parameter types convertions
@app.get("/items/c/{item_id}")
async def red_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id" : item_id}
    if q:
        item.update({"q" : q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# Multiple path and query params
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# Requiered paramenters
@app.get("/items/r/{item_id}")
async def read_user_item(item_id: str, needy: str = None):
    item = {"item_id" : item_id, "needy" : needy}
    return item