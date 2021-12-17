from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from challenge.dto.segment import Segment, SegmentCreate, SegmentUpdate
from challenge.db import deps
from challenge.services import segment

router = APIRouter()


@router.get(
    "/",
    response_model=List[Segment],
    include_in_schema=True,
    summary="List Segments"
)
def get_segments(db: Session = Depends(deps.get_db)) -> List[Segment]:
    return segment.ServiceSegment.get_segments(db)


@router.get(
    "/{id}",
    response_model=Segment,
    include_in_schema=True,
    summary="Get a Segment"
)
def get_segment(db: Session = Depends(deps.get_db), id: int = None) -> Segment:
    return segment.ServiceSegment.get_segment(db, id)


@router.post(
    "/",
    response_model=Segment,
    status_code=201,
    summary="Create a Segment"
)
def createSegment(
        *,
        db: Session = Depends(deps.get_db),
        segmentIn: SegmentCreate
) -> Segment:
    return segment.ServiceSegment.create_segment(db, segmentIn)


@router.put(
    "/{segment_id}",
    response_model=Segment,
    summary="Update a Segment"
)
def updateSegment(
    *,
    db: Session = Depends(deps.get_db),
    segment_id: int,
    segment_in: SegmentUpdate
) -> Segment:
    return segment.ServiceSegment.update_segment(db, segment_id, segment_in)


@router.delete(
    "/{id}",
    include_in_schema=True,
    summary="Delete a segment"
)
def deleteTag(
    db: Session = Depends(deps.get_db),
    id: int = None
) -> Any:
    return segment.ServiceSegment.delete_segment(db, id)
