from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import SensorReading
from app.schemas import SensorReadingCreate, SensorReading

router = APIRouter(prefix="/sensors", tags=["sensors"])


@router.post("/", response_model=SensorReading)
async def create_reading(
    reading: SensorReadingCreate, db: AsyncSession = Depends(get_db)
):
    db_reading = SensorReading(**reading.model_dump())
    db.add(db_reading)
    await db.flush()
    await db.refresh(db_reading)
    return db_reading


@router.get("/", response_model=list[SensorReading])
async def list_readings(
    vehicle_id: str | None = None,
    limit: int = 50,
    db: AsyncSession = Depends(get_db),
):
    stmt = select(SensorReading).order_by(SensorReading.timestamp.desc()).limit(limit)
    if vehicle_id:
        stmt = stmt.where(SensorReading.vehicle_id == vehicle_id)
    result = await db.execute(stmt)
    return result.scalars().all()


@router.get("/{reading_id}", response_model=SensorReading)
async def get_reading(reading_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(SensorReading).where(SensorReading.id == reading_id)
    )
    reading = result.scalar_one_or_none()
    if not reading:
        raise HTTPException(status_code=404, detail="Reading not found")
    return reading
