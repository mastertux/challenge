from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from typing import Any, Dict, Optional, List, Union
from challenge.repositories.base import CreateSchemaType, RepositoryBase
from challenge.models.user import User
from challenge.models.tag import Tag
from challenge.dto.user import UserCreate, UserUpdate
from challenge.models.tag import association_table
from sqlalchemy.sql import text


class RepositoryUser(RepositoryBase[User, UserCreate, UserUpdate]):
    def get_user_filtred(
        self,
        db: Session,
        *,
        filter: str
    ) -> Optional[List[User]]:
        try:
            return db.query(User).join((Tag, User.tags)).filter(
                text(filter)
            ).all()
        except Exception as e:
            raise HTTPException(
                status_code=401,
                detail=f"{e}"
            )

    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create_user(self, db: Session, *, user: User) -> User:
        tags = user.tags
        del(user.tags)
        user_db = self.create(db, obj_in=user)

        for u in tags:
            statement = association_table.insert().values(
                user_id=user_db.id,
                tag_id=u
            )
            db.execute(statement)
            db.commit()
        return user_db

    def update(
        self,
        db: Session,
        *,
        db_obj: UserUpdate,
        obj_in: Union[CreateSchemaType, Dict[str, Any]]
    ) -> User:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        db.query(association_table).filter(
            text(f"user_id = {db_obj.id}")
        ).delete()
        db.commit()

        for i in obj_in.tags:
            statement = association_table.insert().values(
                user_id=db_obj.id,
                tag_id=i
            )
            db.execute(statement)
            db.commit()
        db.refresh(db_obj)
        return db_obj


repository_user = RepositoryUser(User)
