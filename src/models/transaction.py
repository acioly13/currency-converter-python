from sqlalchemy import Column, Integer, String, Float, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    from_currency = Column(String(3), nullable=False)
    to_currency = Column(String(3), nullable=False)
    from_value = Column(Float, nullable=False)
    to_value = Column(Float, nullable=False)
    rate = Column(Float, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
