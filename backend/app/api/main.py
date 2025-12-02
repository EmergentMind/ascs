from fastapi import APIRouter

from app.api.routes import visions, outlooks

api_router = APIRouter()

api_router.include_router(visions.router)
api_router.include_router(outlooks.router)

