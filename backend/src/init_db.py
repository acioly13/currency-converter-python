import asyncio
from src.db import engine
from src.models.transaction import Base
from src.logger import logger


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.success("✅ Database initialized successfully!")


if __name__ == "__main__":
    asyncio.run(init_db())
