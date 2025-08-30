from pydantic import BaseModel, ConfigDict
from datetime import datetime


class TransactionCreate(BaseModel):
    user_id: int
    from_currency: str
    to_currency: str
    amount: float


class TransactionRead(BaseModel):
    id: int
    user_id: int
    from_currency: str
    to_currency: str
    from_value: float
    to_value: float
    rate: float
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)
