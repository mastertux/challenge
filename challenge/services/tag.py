from typing import Any, List
from fastapi.exceptions import HTTPException
from challenge.dto.tag import Tag
from challenge.repositories import tag
from sqlalchemy.orm import Session


class ServiceTag():
    def get_tags(db: Session = None) -> List[Tag]:
        return tag.repository_tag.get_multi(db)

    def create_tag(db: Session = None, tag_in: Tag = None) -> Tag:
        return tag.repository_tag.create(db, obj_in=tag_in)

    def get_tag(db: Session = None, id: int = None):
        tag_db = tag.repository_tag.get(db, id)

        if not tag_db:
            raise HTTPException(
                status_code=404,
                detail="The tag with this id does not exist in the system"
            )
        return tag_db

    def update_tag(
        db: Session = None,
        tag_id: int = None,
        tag_in: Tag = None
    ) -> Tag:
        tag_db = tag.repository_tag.get(db, id=tag_id)
        if not tag_db:
            raise HTTPException(
                status_code=404,
                detail="The tag with this id does not exist in the system"
            )

        if tag.repository_tag.get_by_name(db, name=tag_in.name):
            raise HTTPException(
                status_code=400,
                detail="Tag already registered"
            )

        return tag.repository_tag.update(
            db,
            db_obj=tag_db,
            obj_in=tag_in
        )

    def delete(db: Session = None, id: int = None) -> Any:
        tag_db = tag.repository_tag.get(db, id=id)

        if not tag_db:
            raise HTTPException(
                status_code=404,
                detail="The tag with this id does not exist in the system"
            )
        try:
            return tag.repository_tag.remove(db, id=id)
        except Exception as e:
            raise HTTPException(
                status_code=409,
                detail=f"{e}"
            )
