from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def get_text(db: Session, text_id: int):
    return db.query(models.Text).filter(models.Text.id == text_id).first()


def get_text_by_url(db: Session, url: str):
    return db.query(models.Text).filter(models.Text.url == url).first()


def get_texts(db: Session):
    return db.query(models.Text).all()


def add_personalizations_to_user(db: Session, texts: list[models.Text], user_id: int):
    for t in texts:
        if (
            db.query(models.Personalization)
            .filter(
                models.Personalization.user_id == user_id
                and models.Personalization.text_id == t.id
            )
            .first()
        ):
            db.add(models.Personalization(user_id=user_id, text_id=t.text))
    db.commit()


def create_user(db: Session, user: schemas.User):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_text(db: Session, text: schemas.Text):
    db_text = models.Text(**text.dict())
    db.add(db_text)
    db.commit()
    db.refresh(db_text)
    return db_text


def create_rating(db: Session, rating: schemas.Rating):
    db_rating = models.Rating(**rating.dict())
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating
