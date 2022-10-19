from typing import Union
from fastapi import FastAPI
from enum import Enum

# Predefined options class example
class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'letnet'

# create FastAPI basiclication
app = FastAPI()

# Take care about endpoints orders
# Take care about endpoints redefining operations
# https://fastapi.tiangolo.com/tutorial/path-params/#order-matters

# Default Route
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Route with parameter (item_id)
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item id" : item_id}

# Predefined values options with Enum
@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):

    # Compare with enumerate member
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep learning FTW!"}
    # Compare enumeration values
    if model_name.value == 'letnet':
        return {"model_name": model_name, "message": "LeCCN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}