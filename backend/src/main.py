from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .routes import transactions
from .db import init_db
from .logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    logger.info(
        "\n✅ API is running at: http://localhost:8000/docs \n"
        "✅ Frontend is available at: http://localhost:5173 \n"
    )
    yield

app = FastAPI(title="Currency Converter API", lifespan=lifespan)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transactions.router)
