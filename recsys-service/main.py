from fastapi import FastAPI
from models import Request
from recsys import RecSys

app = FastAPI()

@app.post("/score/", response_model=float)
async def score(request: Request):
    return RecSys.score(request.user.id, request.text.id)
