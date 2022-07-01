from typing import Optional

from pydantic import BaseModel


class TokenData(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class CreateProfile(BaseModel):
    city: str


class CreatedProfile(BaseModel):
    id: int
    city: str
    user_id: int

    class Config:
        orm_mode = True


class CreateSubscription(BaseModel):
    name: str


class CreatedSubscription(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

