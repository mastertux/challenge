from typing import Any, List
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from challenge.dto.user import User
from challenge.repositories import user


class ServiceUser:
    def get_users(db) -> List[User]:
        return user.repository_user.get_multi(db)

    def get_user(db: Session = None, id: int = None) -> User:
        user_db = user.repository_user.get(db, id=id)

        if not user_db:
            raise HTTPException(
                status_code=404,
                detail="The user with this id does not exist in the system"
            )
        return user_db

    def get_filtred_users(
        db,
        filter: str = None
    ) -> List[User]:
        return user.repository_user.get_user_filtred(db, filter=filter)

    def create_user(
        db: Session = None,
        user_in: User = None
    ) -> User:
        db_user = user.repository_user.get_by_email(
            db,
            email=user_in.email
        )

        if db_user:
            raise HTTPException(
                status_code=400,
                detail="User already registered"
            )
        return user.repository_user.create_user(db, user=user_in)

    def delete(db: Session = None, id: int = None) -> Any:
        user_db = user.repository_user.get(db, id=id)

        if not user_db:
            raise HTTPException(
                status_code=404,
                detail="The user with this id does not exist in the system"
            )
        try:
            return user.repository_user.remove(db, id=id)
        except Exception as e:
            raise HTTPException(
                status_code=409,
                detail=f"{e}"
            )

    def update_user(
        db: Session = None,
        user_id: int = None,
        user_in: User = None
    ) -> User:
        user_db = user.repository_user.get(db, id=user_id)
        if not user_db:
            raise HTTPException(
                status_code=404,
                detail="The user with this id does not exist in the system"
            )

        email_existis = user.repository_user.get_by_email(
            db,
            email=user_in.email
        )

        if email_existis and user_db.id != email_existis.id:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

        return user.repository_user.update(
            db,
            db_obj=user_db,
            obj_in=user_in
        )
