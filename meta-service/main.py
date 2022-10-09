from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas, utils, settings
from database import SessionLocal, engine

import requests

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.UserFull)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_user(db=db, user=user)


@app.post("/texts/", response_model=schemas.TextFull)
def create_text(text: schemas.Text, db: Session = Depends(get_db)):
    db_text = crud.get_text_by_url(db, url=text.url)
    if db_text:
        raise HTTPException(status_code=400, detail="Text already registered")
    t = utils.get_text_embedding(crud.create_text(db=db, text=text))
    return t


@app.post("/news/", response_model=list[schemas.TextFull])
def get_news(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    personalizations = user.personalizations
    if len(user.personalizations) < 10:
        crud.add_personalizations_to_user(db, crud.get_texts(), user_id)
    db.refresh(user)
    personalizations = user.personalizations

    texts = [p.text for p in personalizations]
    data = [
        {
            "id": t.id,
            "data": utils.str_to_list(t.embedded_title)[:100]
            + utils.str_to_list(t.embedded_text),
        }
        for t in texts
    ]

    vectors_ids = [
        e["id"]
        for e in requests.post(settings.CLUSTERIZATION_SERVICE_URL, json=data).json()
    ]

    for p in personalizations:

        if p.text.id not in vectors_ids:
            continue

        if not p.is_scored:
            p.score = utils.get_personalization_score()
            p.is_scored = True
            p.save()

    res = sorted(personalizations, key=lambda x: x.score)
    res = [e.text for e in res]

    return res
