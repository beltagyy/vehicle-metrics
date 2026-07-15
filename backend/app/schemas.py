from datetime import datetime

from pydantic import BaseModel


class SensorReadingBase(BaseModel):
    vehicle_id: str
    sensor_type: str
    value: float
    unit: str


class SensorReadingCreate(SensorReadingBase):
    pass


class SensorReading(SensorReadingBase):
    id: int
    timestamp: datetime

    model_config = {"from_attributes": True}
