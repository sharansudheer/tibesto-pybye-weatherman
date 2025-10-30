from fastapi import FastAPI
from app.api.routes_json_tree import router as json_tree_router
from app.api.error_handlers import register_error_handlers

from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/home/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


