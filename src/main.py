from fastapi import FastAPI
from contextlib import asynccontextmanager
from .routes import transactions
from .db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print("\n API is running at: http://localhost:8000\n")
    yield

app = FastAPI(title="Currency Converter API", lifespan=lifespan)

app.include_router(transactions.router)
