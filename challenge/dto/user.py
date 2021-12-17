from pydantic import BaseModel
from typing import List
from enum import Enum
import datetime
from challenge.dto.tag import Tag


class SexEnum(str, Enum):
    male = 'male'
    female = 'female'


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    sex: SexEnum
    birth_date: datetime.date
    admission_date: datetime.date
    is_active: bool
    segment_id: int
    tags: List[Tag]


class UserCreate(UserBase):
    tags: List[int]
    pass


class UserUpdate(UserBase):
    tags: List[int]
    pass


class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserInDB(UserInDBBase):
    pass


class User(UserInDBBase):
    pass
