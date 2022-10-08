from pydantic import BaseModel


class NewsModel(BaseModel):
    maintext: str
    title: str
