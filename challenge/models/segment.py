from sqlalchemy import Column, Integer, String
from challenge.db.base_class import Base


class Segment(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)
