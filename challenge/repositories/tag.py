from typing import Optional
from sqlalchemy.orm import session
from challenge.repositories.base import RepositoryBase
from challenge.models.tag import Tag
from challenge.dto.tag import TagCreate, TagUpdate


class RepositoryTag(RepositoryBase[Tag, TagCreate, TagUpdate]):
    def get_by_name(self, db: session, *, name: str) -> Optional[Tag]:
        return db.query(Tag).filter(Tag.name == name).first()


repository_tag = RepositoryTag(Tag)
