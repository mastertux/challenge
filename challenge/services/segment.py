from typing import List
from fastapi.exceptions import HTTPException
from challenge.dto.segment import Segment
from challenge.repositories import segment
from sqlalchemy.orm import Session


class ServiceSegment():
    def get_segments(db: Session = None) -> List[Segment]:
        return segment.repository_segment.get_multi(db)

    def get_segment(db: Session = None, id: int = None) -> Segment:
        segment_db = segment.repository_segment.get(db, id=id)

        if not segment_db:
            raise HTTPException(
                status_code=404,
                detail="The segment with this id does not exist in the system"
            )
        return segment_db

    def create_segment(
        db: Session = None,
        segmentIn: Segment = None
    ) -> Segment:
        db_segment = segment.repository_segment.get_by_name(
            db,
            name=segmentIn.name
        )

        if db_segment:
            raise HTTPException(
                status_code=400,
                detail="Segment already registered"
            )
        return segment.repository_segment.create(db, obj_in=segmentIn)

    def update_segment(
        db: Session = None,
        segment_id: int = None,
        segment_in: Segment = None
    ) -> Segment:
        segment_db = segment.repository_segment.get(db, id=segment_id)

        if not segment_db:
            raise HTTPException(
                status_code=404,
                detail="The segment with this id does not exist in the system"
            )

        if segment.repository_segment.get_by_name(db, name=segment_in.name):
            raise HTTPException(
                status_code=400,
                detail="Segment already registered"
            )

        return segment.repository_segment.update(
            db,
            db_obj=segment_db,
            obj_in=segment_in
        )

    def delete_segment(db: Session = None, id: int = None):
        segment_db = segment.repository_segment.get(db, id=id)

        if not segment_db:
            raise HTTPException(
                status_code=404,
                detail="The segment with this id does not exist in the system"
            )

        try:
            return segment.repository_segment.remove(db, id=id)
        except Exception as e:
            raise HTTPException(
                status_code=409,
                detail=f"{e}"
            )
