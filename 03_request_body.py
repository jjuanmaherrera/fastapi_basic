from operator import itemgetter
from typing import Union
from fastapi import FastAPI

# Use pydantic library
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()

# Default route
@app.get("/")
async def root():
    return {"message" : "Default Route" }

# Use model Item
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()

    # If not null calculate tax
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax" : price_with_tax})
    
    # Return new object
    return item_dict

# Request body with path parameter
@app.put("/item/{item_id}")
async def create_item(item_id: int, item : Item):
    return {"item_id": item_id, **item.dict()}

# Request body with path and query parameters
@app.put("/items/q/{item_id}")
async def create_item(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result