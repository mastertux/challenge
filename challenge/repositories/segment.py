from typing import Optional
from sqlalchemy.orm import Session
from challenge.repositories.base import RepositoryBase
from challenge.models.segment import Segment
from challenge.dto.segment import SegmentCreate, SegmentUpdate


class RepositorySegment(RepositoryBase[Segment, SegmentCreate, SegmentUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Segment]:
        return db.query(Segment).filter(Segment.name == name).first()


repository_segment = RepositorySegment(Segment)
