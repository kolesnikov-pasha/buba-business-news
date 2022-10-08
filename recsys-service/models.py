from pydantic import BaseModel

class User(BaseModel):
    id: int

class Text(BaseModel):
    id: int

class Request(BaseModel):
    user: User
    text: Text
