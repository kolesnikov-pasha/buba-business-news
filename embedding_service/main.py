from typing import Union

from fastapi import FastAPI
from models import NewsModel
from embedder import Embedder
from pydantic import BaseModel


class Item(BaseModel):
    maintext: str
    title: str


app = FastAPI()


@app.post("/", response_model=list[float])
async def root(news_model: NewsModel):
    res = Embedder.embed_news(news_model)
    return res
