from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .routes import transactions
from .db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print("\n✅ API is running at: http://localhost:8000\n")
    yield


app = FastAPI(title="Currency Converter API", lifespan=lifespan)

# Configuração CORS para permitir frontend
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # pode ser ["*"] em dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transactions.router)
