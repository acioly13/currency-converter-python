from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    user_id: int
    from_currency: str
    to_currency: str
    from_value: float
    to_value: float
    rate: float

class TransactionRead(TransactionCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
