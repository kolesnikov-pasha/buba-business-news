from fastapi import FastAPI
from pydantic import BaseModel
import random
from sklearn.cluster import DBSCAN
import numpy as np

app = FastAPI()


class Vector(BaseModel):
    id: int
    data: list[float]



@app.post("/", response_model=list[Vector])
async def root(vectors: list[Vector]):
    X = [[] for i in range(len(vectors))]
    for i in range(len(vectors)):
        X[i] = vectors[i].data
    X = np.array(X)
    dbscan = DBSCAN(eps=0.12, min_samples=3, metric='cosine')
    db_clust = dbscan.fit_predict(X)
    result = []
    num_clusters = db_clust.max()
    for i in range(num_clusters, num_clusters - min(3, num_clusters), -1):
        for j, vec in enumerate(vectors):
            if db_clust[j] == i:
                result.append(vec)
                break
    return result # возвращает не больше трех новостей