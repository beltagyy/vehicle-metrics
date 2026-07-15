from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
import redis.asyncio as redis

from app.database import get_db
from app.cache import get_redis

router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check(
    db: AsyncSession = Depends(get_db),
    redis_client: redis.Redis = Depends(get_redis),
):
    checks = {"status": "healthy", "services": {}}

    try:
        await db.execute(text("SELECT 1"))
        checks["services"]["postgres"] = "ok"
    except Exception as e:
        checks["services"]["postgres"] = f"error: {str(e)}"
        checks["status"] = "degraded"

    try:
        await redis_client.ping()
        checks["services"]["redis"] = "ok"
    except Exception as e:
        checks["services"]["redis"] = f"error: {str(e)}"
        checks["status"] = "degraded"

    return checks
