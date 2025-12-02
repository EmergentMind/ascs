from typing import Annotated
from fastapi import APIRouter, Query, Path, HTTPException
from sqlmodel import select

from app.api.dependencies import SessionDep
from app.models import Tags, Vision, VisionPublic, VisionsPublic

router = APIRouter(
        prefix="/visions",
        tags=["visions"],
        )

@router.get("/", response_model=VisionsPublic, tags=[Tags.visions])
async def read_visions(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
        ):
    visions = session.exec(select(Vision).offset(offset).limit(limit)).all()
    return visions

@router.get("/{vision_id}", response_model=VisionPublic, tags=[Tags.visions])
async def read_vision(
        vision_id: Annotated[int, Path(title="The id of the vision to get")],
        session: SessionDep
        ):
    vision = session.get(Vision, vision_id)

    #NOTE: we can remove this once ids are automatically set with UUIDs
    if vision is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return vision

@router.post(
        "/",
        response_model=VisionPublic,
        tags=[Tags.visions],
        summary="Create a new vision",
        )
async def create_vision(vision: Vision, session: SessionDep) -> Vision:
    """
    Create a vision with all of the information:
    - title
    - description
    """    
    session.add(vision)
    session.commit()
    session.refresh(vision)
    return vision

