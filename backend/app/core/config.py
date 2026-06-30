from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "CareerPilot AI"
    DATABASE_URL: str = "postgresql+psycopg://careerpilot:careerpilot123@localhost:5432/careerpilot"

    class Config:
        env_file = ".env"


settings = Settings()