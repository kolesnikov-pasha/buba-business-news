from fastapi import FastAPI
from pydantic import BaseModel
import random


app = FastAPI()

class Vector(BaseModel):
    id: int
    data: list[float]


@app.post("/", response_model=list[list[int]])
async def root(vectors: list[Vector]):
    random.shuffle(vectors)
    clusters_start_end = [(0, len(vectors) // 3), (len(vectors) // 3, len(vectors) * 2 // 3), (len(vectors) * 2 // 3, len(vectors))]
    clusters = []
    for start, end in clusters_start_end:
        clusters.append([e.id for e in vectors[start:end]])

    return clusters
