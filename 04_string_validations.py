from operator import truediv
from typing import Union, List
from unittest import result

# Import Query for data validation
from fastapi import FastAPI, Query

app = FastAPI()

# Default root
@app.get("/")
async def root():
    return {"message": "default route"}

# Add validation
@app.get("/items/")
# Validate no more than 50 characters on "q" optional parameter
# Use query as the default value
# Declare metadata for openAPI
async def read_items(
    q: Union[str, None] = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex = '^fixedquery$',
        alias = "item-query",
        # mark a query parameter as deprecated without disabled it
        deprecated = True
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Receive a list of values
@app.get("/items/list/")
async def read_items(
    q: Union[List[str], None] = Query(default=None),
    # Add a query parameter but exclude from OpenAPI schema
    hidden_query: Union[str, None] = Query(default=None, include_in_schema=False)
    ):
    query_items = {"q": q}
    return query_items