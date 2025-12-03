from fastapi import APIRouter

from app.api.visions import visions
from app.api.outlooks import outlooks

api_router = APIRouter()

api_router.include_router(visions.router)
api_router.include_router(outlooks.router)

