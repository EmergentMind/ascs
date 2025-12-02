from typing import Annotated
from fastapi import APIRouter, Query, Path
from sqlmodel import Session, select

from app.api.dependencies import SessionDep
from app.models import Tags, Vision

router = APIRouter(
        prefix="/visions",
        tags=["visions"],
        )

@router.get("/", tags=[Tags.visions])
async def read_visions(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
        ):
    visions = session.exec(select(Vision).offset(offset).limit(limit)).all()
    return visions

@router.get("/{vision_id}", tags=[Tags.visions])
async def read_vision(
        vision_id: Annotated[int, Path(title="The id of the vision to get")],
        session: SessionDep
        ):
    vision = session.get(Vision, vision_id)
    return vision

@router.post(
        "/",
        response_model=Vision,
        tags=[Tags.visions],
        summary="Create a new vision",
        )
async def create_vision(vision: Vision, session: SessionDep) -> Vision:
    """
    Create a vision with all of the information:
    - TODO
    """    
    session.add(vision)
    session.commit()
    session.refresh(vision)
    return vision

