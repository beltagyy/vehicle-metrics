from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "VehicleMetrics"
    debug: bool = False

    postgres_user: str = "vehicle"
    postgres_password: str = "password"
    postgres_db: str = "vehiclemetrics"
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    redis_host: str = "localhost"
    redis_port: int = 6379

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    @property
    def redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}/0"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
