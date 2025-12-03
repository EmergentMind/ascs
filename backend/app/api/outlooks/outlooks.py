from typing import Annotated, Any
from fastapi import APIRouter, Query, Path, HTTPException
from sqlmodel import select, func

from app.api.dependencies import SessionDep
from app.models import Outlook, OutlookCreate, OutlookPublic, OutlooksPublic

router = APIRouter(
        prefix="/outlooks",
        tags=["outlooks"],
        )

@router.get("/", response_model=OutlooksPublic)
async def read_outlooks(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
        ) -> Any:
    count_statement = select(func.count()).select_from(Outlook)
    count = session.exec(count_statement).one()
    statement = select(Outlook).offset(offset).limit(limit)

    outlooks = session.exec(statement).all()
    outlooks_public = [OutlookPublic.model_validate(o) for o in outlooks]

    return OutlooksPublic(data=outlooks_public, count=count)

@router.get("/{outlook_id}", response_model=OutlookPublic)
async def read_outlook(
        outlook_id: Annotated[int, Path(title="The id of the outlook to get")],
        session: SessionDep
        ):
    outlook = session.get(Outlook, outlook_id)

    #NOTE: we can remove this once ids are automatically set with UUIDs
    if outlook is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return outlook

@router.post( "/", response_model=OutlookPublic, summary="Create a new outlook",)
async def create_outlook(outlook_in: OutlookCreate, session: SessionDep) -> Outlook:
    """
    Create an outlook with all of the information:
    - start_year
    """    
    outlook = Outlook.model_validate(outlook_in)

    session.add(outlook)
    session.commit()
    session.refresh(outlook)
    return outlook
