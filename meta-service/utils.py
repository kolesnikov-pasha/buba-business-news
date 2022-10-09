from sqlalchemy.orm import Session

import models, settings
import requests


def get_text_embedding(db: Session, text: models.Text):
    data = {"maintext": text.text, "title": text.title}
    response = requests.post(settings.EMBEDDING_SERVICE_URL, json=data).json()
    text.embedded_title = response[:312]
    text.embedded_text = response[:312]
    db.commit()
    db.refresh(text)
    return text


def get_personalization_score():
    pass


def update_user_personalization():
    pass
