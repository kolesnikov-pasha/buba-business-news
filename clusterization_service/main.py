from fastapi import FastAPI
from pydantic import BaseModel
import random
import pickle as pkl
from sklearn.cluster import DBSCAN
import numpy as np

app = FastAPI()


class Vector(BaseModel):
    id: int
    data: list[float]



@app.post("/", response_model=list[Vector])
async def root(vectors: list[Vector]):
    clusters = []
    X = [[] for i in range(len(vectors))]
    for i in range(len(vectors)):
        X[i] = vectors[i].data
    X = np.array(X)
    dbscan = DBSCAN(eps=0.05, min_samples=2, metric='cosine')
    db_clust = dbscan.fit_predict(X)
    result = []
    used = set()
    for i, vec in enumerate(vectors):
        if db_clust[i] == -1:
            result.append(vec)
            continue
        if db_clust[i] not in used:
            used.add(db_clust[i])
            result.append(vec)
    return result
