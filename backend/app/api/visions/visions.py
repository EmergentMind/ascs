from typing import Annotated, Any
from fastapi import APIRouter, Query, Path, HTTPException
from sqlmodel import select, func

from app.api.dependencies import SessionDep
from app.models import Vision, VisionCreate, VisionPublic, VisionsPublic

router = APIRouter(
        prefix="/visions",
        tags=["visions"],
        )

@router.get("/", response_model=VisionsPublic)
async def read_visions(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
        ) -> Any:
    count_statement = select(func.count()).select_from(Vision)
    count = session.exec(count_statement).one()
    statement = select(Vision).offset(offset).limit(limit)

    visions = session.exec(statement).all()
    visions_public = [VisionPublic.model_validate(v) for v in visions]

    return VisionsPublic(data=visions_public, count=count)

@router.get("/{vision_id}", response_model=VisionPublic)
async def read_vision(
        vision_id: Annotated[int, Path(title="The id of the vision to get")],
        session: SessionDep
        ):
    vision = session.get(Vision, vision_id)

    #NOTE: we can remove this once ids are automatically set with UUIDs
    if vision is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return vision

@router.post( "/", response_model=VisionPublic, summary="Create a new vision",)
async def create_vision(vision_in: VisionCreate, session: SessionDep) -> Vision:
    """
    Create a vision with all of the information:
    - title
    - description
    """    
    vision = Vision.model_validate(vision_in)

    session.add(vision)
    session.commit()
    session.refresh(vision)
    return vision

