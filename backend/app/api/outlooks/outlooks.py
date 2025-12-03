from typing import Annotated
from fastapi import APIRouter, Query, Path, HTTPException
from sqlmodel import select

from app.api.dependencies import SessionDep
from app.models import Tags, Outlook, OutlookPublic, OutlooksPublic

router = APIRouter(
        prefix="/outlooks",
        tags=["outlooks"],
        )

@router.get("/", response_model=OutlooksPublic, tags=[Tags.outlooks])
async def read_outlooks(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
        ):
    outlooks = session.exec(select(Outlook).offset(offset).limit(limit)).all()
    return outlooks

@router.get("/{outlook_id}", response_model=OutlookPublic, tags=[Tags.outlooks])
async def read_outlook(
        outlook_id: Annotated[int, Path(title="The id of the outlook to get")],
        session: SessionDep
        ):
    outlook = session.get(Outlook, outlook_id)

    #NOTE: we can remove this once ids are automatically set with UUIDs
    if outlook is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return outlook

@router.post(
        "/",
        response_model=OutlookPublic,
        tags=[Tags.outlooks],
        summary="Create a new outlook",
        )
async def create_outlook(outlook: Outlook, session: SessionDep) -> Outlook:
    """
    Create an outlook with all of the information:
    - start_year
    """    
    session.add(outlook)
    session.commit()
    session.refresh(outlook)
    return outlook
