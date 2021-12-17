from fastapi import APIRouter
from challenge.controllers.api_v1 import user, segment, tag

api_router = APIRouter()
api_router.include_router(
    segment.router,
    prefix="/segments",
    tags=["Segments"]
)
api_router.include_router(tag.router, prefix="/tags", tags=["Tags"])
api_router.include_router(user.router, prefix="/users", tags=["Users"])
