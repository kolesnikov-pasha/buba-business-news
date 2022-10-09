from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
    Boolean,
)
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    role = Column(String, index=True)

    rates = relationship("Rating", back_populates="user")
    personalizations = relationship("Personalization", back_populates="user")


class Text(Base):
    __tablename__ = "texts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    text = Column(String, index=True)
    source_domain = Column(String, index=True)
    source_id = Column(String, index=True)
    is_ready = Column(Boolean, index=True)
    url = Column(String, index=True, unique=True)
    embedded_title = Column(String, default="")
    embedded_text = Column(String, default="")

    rates = relationship("Rating", back_populates="text")
    personalizations = relationship("Personalization", back_populates="text")


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    text_id = Column(Integer, ForeignKey("texts.id"))

    user = relationship("User", back_populates="rates")
    text = relationship("Text", back_populates="rates")


class Personalization(Base):
    __tablename__ = "personalization"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Float, primary_key=True)
    is_scored = Column(Boolean, index=True, default=False)
    text_id = Column(Integer, ForeignKey("texts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    text = relationship("Text", back_populates="personalizations")
    user = relationship("User", back_populates="personalizations")
