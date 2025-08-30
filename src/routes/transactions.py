from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
import os
import currencyapicom

from ..db import get_session
from ..models.transaction import Transaction
from ..schemas.transaction import TransactionCreate, TransactionRead

router = APIRouter()

CURRENCY_API_KEY = os.getenv("CURRENCY_API_KEY")
client = currencyapicom.Client(CURRENCY_API_KEY)


@router.post("/convert", response_model=TransactionRead)
async def convert(transaction: TransactionCreate, session: AsyncSession = Depends(get_session)):
    print("➡️ /convert called")
    print("Input transaction:", transaction.model_dump())

    try:
        print(f"Fetching rate for {transaction.from_currency} -> {transaction.to_currency}")
        result = client.latest(transaction.from_currency, currencies=[transaction.to_currency])
        print("Currency API result:", result)

        rate = result["data"][transaction.to_currency]["value"]
        print("Rate obtained:", rate)

    except Exception as e:
        print("❌ Currency API error:", str(e))
        raise HTTPException(status_code=500, detail=f"Currency API error: {str(e)}")

    from_value = transaction.amount
    to_value = transaction.amount * rate
    print(f"Converting {from_value} {transaction.from_currency} -> {to_value} {transaction.to_currency}")

    db_transaction = Transaction(
        user_id=transaction.user_id,
        from_currency=transaction.from_currency,
        to_currency=transaction.to_currency,
        from_value=from_value,
        to_value=to_value,
        rate=rate
    )

    session.add(db_transaction)
    await session.commit()
    await session.refresh(db_transaction)

    print("✅ Transaction saved:", db_transaction.__dict__)
    return db_transaction


@router.get("/transactions", response_model=List[TransactionRead])
async def get_transactions(userId: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Transaction).where(Transaction.user_id == userId))
    transactions = result.scalars().all()
    return transactions
