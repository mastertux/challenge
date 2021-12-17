from typing import Any, List, Optional
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from challenge.dto.user import User, UserCreate, UserUpdate
from challenge.db import deps
from challenge.services.user import ServiceUser
router = APIRouter()


@router.get(
    "/",
    response_model=List[User],
    include_in_schema=True,
    description="List and filter users"
)
def getUsers(
    db: Session = Depends(deps.get_db),
    filter: Optional[str] = None
) -> Any:
    try:
        if filter is None:
            return ServiceUser.get_users(db)
        return ServiceUser.get_filtred_users(db, filter)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=e
        )


@router.get(
    "/{id}",
    include_in_schema=True,
    description="Get a user"
)
def getUser(
    db: Session = Depends(deps.get_db),
    id: int = None
) -> Any:
    return ServiceUser.get_user(db, id)


@router.post(
    "/",
    response_model=User,
    status_code=201,
    summary="Create a user"
)
def createUser(
        *,
        db: Session = Depends(deps.get_db),
        userIn: UserCreate
) -> User:
    return ServiceUser.create_user(db, userIn)


@router.delete(
    "/{id}",
    include_in_schema=True,
    description="Delete a user"
)
def deleteUser(
    db: Session = Depends(deps.get_db),
    id: int = None
) -> Any:
    return ServiceUser.delete(db, id)


@router.put(
    "/{tag_id}",
    response_model=User,
    summary="Update a user"
)
def updateUser(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    user_in: UserUpdate
) -> User:
    return ServiceUser.update_user(db, user_id, user_in)
