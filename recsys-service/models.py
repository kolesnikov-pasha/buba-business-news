from pydantic import BaseModel

class User(BaseModel):
    id: str

class Text(BaseModel):
    source_domain: str
    id: str

class Request(BaseModel):
    user: User
    text: Text
