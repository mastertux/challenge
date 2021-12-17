from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    Date,
    DateTime,
    ForeignKey
)
from sqlalchemy.sql import func
from challenge.db.base_class import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False, index=True, )
    last_name = Column(String(100), nullable=False, index=True)
    email = Column(String, nullable=False, index=True, unique=True)
    birth_date = Column(Date, nullable=False, index=True)
    admission_date = Column(Date, nullable=False, index=True)
    is_active = Column(Boolean, default=True)
    sex = Column(String, nullable=False, index=True)
    last_sign_in_at = Column(DateTime, nullable=True, default=func.now())
    segment_id = Column(Integer, ForeignKey('segment.id'), nullable=False)
