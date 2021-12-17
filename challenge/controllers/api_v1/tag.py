from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from challenge.dto.tag import Tag, TagCreate, TagUpdate
from challenge.db import deps
from challenge.services import tag

router = APIRouter()


@router.get(
    "/",
    response_model=List[Tag],
    include_in_schema=True,
    summary="List tags"
)
def getTags(db: Session = Depends(deps.get_db)) -> List[Tag]:
    return tag.ServiceTag.get_tags(db)


@router.get(
    "/{id}",
    response_model=Tag,
    include_in_schema=True,
    summary="Get a tag"
)
def getTag(db: Session = Depends(deps.get_db), id: int = None) -> Tag:
    return tag.ServiceTag.get_tag(db, id)


@router.post(
    "/",
    response_model=Tag,
    status_code=201,
    summary="Create a tag"
)
def createTag(
        *,
        db: Session = Depends(deps.get_db),
        tag_in: TagCreate
) -> Tag:
    return tag.ServiceTag.create_tag(db, tag_in)


@router.put(
    "/{tag_id}",
    response_model=Tag,
    summary="Update a tag"
)
def updateTag(
    *,
    db: Session = Depends(deps.get_db),
    tag_id: int,
    tag_in: TagUpdate
) -> Tag:
    return tag.ServiceTag.update_tag(db, tag_id, tag_in)


@router.delete(
    "/{id}",
    include_in_schema=True,
    description="Delete a tag"
)
def deleteTag(
    db: Session = Depends(deps.get_db),
    id: int = None
) -> Any:
    return tag.ServiceTag.delete(db, id)
