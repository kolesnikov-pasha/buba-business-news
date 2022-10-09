from re import L, S
from typing import Union
from unittest.mock import Base

from pydantic import BaseModel


class User(BaseModel):
    name: str
    role: str


class UserFull(User):
    id: int

    class Config:
        orm_mode = True


class Text(BaseModel):
    title: str
    text: str
    source_domain: str
    source_id: str
    url: str


class TextFull(Text):
    id: int
    embedded_title: list[float]
    embedded_text: list[float]

    class Config:
        orm_mode = True


class Rating(BaseModel):
    rating: int
    text_id: int
    user_id: int
