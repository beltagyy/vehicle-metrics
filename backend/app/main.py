from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routes import health, sensors
from app.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title=settings.app_name,
    description="Autonomous Vehicle Sensor Analytics API",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(health.router)
app.include_router(sensors.router)


@app.get("/")
async def root():
    return {"app": settings.app_name, "version": "0.1.0", "docs": "/docs"}
