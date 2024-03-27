from datetime import datetime

from pydantic import BaseModel


class CardNumberInfo(BaseModel):
    id: int
    card_number: str


class Winner(BaseModel):
    id: int
    card_number: str
    phone_number: str
