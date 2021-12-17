from typing import Optional
from pydantic import BaseModel


class SegmentBase(BaseModel):
    name: str


class SegmentCreate(SegmentBase):
    pass


class SegmentUpdate(SegmentBase):
    pass


class SegmentInDBBase(SegmentBase):
    id: Optional[int]

    class Config:
        orm_mode = True


class SegmentInDB(SegmentInDBBase):
    pass


class Segment(SegmentInDBBase):
    pass
