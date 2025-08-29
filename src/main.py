from fastapi import FastAPI
from .routes import transactions
from .db import init_db

app = FastAPI(title="Currency Converter API")

app.include_router(transactions.router)


@app.on_event("startup")
async def startup_event():
    await init_db()
    print("\n API is running at: http://localhost:8000\n")
