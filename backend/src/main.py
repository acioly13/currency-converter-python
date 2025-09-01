from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .routes import transactions
from .db import init_db
from .logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    logger.info("✅ API is running at: http://localhost:8000")
    yield


app = FastAPI(title="Currency Converter API", lifespan=lifespan)

# CORS
origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transactions.router)
