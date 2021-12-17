from pydantic import BaseSettings, PostgresDsn, validator
from typing import Any, Dict, Optional


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Qulture Challenge"
    SQLALCHEMY_DATABASE_URI: str = None
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///test.db"

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(
        cls,
        v: Optional[str],
        values: Dict[str, Any]
    ) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user="tulio",
            password="tulio",
            host="localhost",
            path="/qulture",
        )

    class Config:
        case_sensitive = True


settings = Settings()
