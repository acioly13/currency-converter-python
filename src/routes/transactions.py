from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
import httpx
import os

from ..db import get_session
from ..models.transaction import Transaction
from ..schemas.transaction import TransactionCreate, TransactionRead

router = APIRouter()

CURRENCY_API_KEY = os.getenv("CURRENCY_API_KEY")


@router.post("/convert", response_model=TransactionRead)
async def convert(transaction: TransactionCreate, session: AsyncSession = Depends(get_session)):
    url = f"https://api.currencyapi.com/v3/latest?apikey={CURRENCY_API_KEY}&currencies={transaction.to_currency}&base_currency={transaction.from_currency}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Currency API error")
        data = response.json()
        rate = data["data"][transaction.to_currency]["value"]

    transaction.to_value = transaction.from_value * rate
    transaction.rate = rate

    db_transaction = Transaction(**transaction.dict())
    session.add(db_transaction)
    await session.commit()
    await session.refresh(db_transaction)
    return db_transaction


@router.get("/transactions", response_model=List[TransactionRead])
async def get_transactions(userId: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Transaction).where(Transaction.user_id == userId))
    transactions = result.scalars().all()
    return transactions
