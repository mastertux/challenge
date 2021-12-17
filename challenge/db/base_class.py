from typing import Any
from sqlalchemy import Column, Date
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base():
    id: Any
    __name__: str
    created_at = Column(Date, default=func.now())
    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
