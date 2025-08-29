from fastapi import FastAPI
from .routes import transactions

app = FastAPI(title="Currency Converter API")

app.include_router(transactions.router)
