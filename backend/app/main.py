from app.core.database import get_session

from fastapi import FastAPI, Path, Depends, Query

from sqlmodel import Field, SQLModel, Session, select 
from typing import Optional, Annotated
from enum import Enum

# temp models
class Tags(Enum):
    visions = "visions"
    outlooks = "outlooks"
    seasons = "seasons"
    users = "users"

class Vision(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(default="Aspirational Vision")
    description: str | None = Field (
            default= None, title="Vision Description", max_length=300
            )
class Outlook(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    start_year: int = Field(gt=0, description="The year that your current Three Year Outlook began.")
    notes: str | None = Field (
            default= None, title="Notes", max_length=300
            )

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

# vision
@app.get("/visions/", tags=[Tags.visions])
async def read_visions(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
        ):
    visions = session.exec(select(Vision).offset(offset).limit(limit)).all()
    return visions

@app.get("/visions/{vision_id}", tags=[Tags.visions])
async def read_vision(
        vision_id: Annotated[int, Path(title="The id of the vision to get")],
        session: SessionDep
        ):
    vision = session.get(Vision, vision_id)
    return vision

@app.post(
        "/visions/",
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

# outlook
@app.get("/outlooks/", tags=[Tags.outlooks])
async def read_outlooks(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
        ):
    outlooks = session.exec(select(Outlook).offset(offset).limit(limit)).all()
    return outlooks

@app.get("/outlooks/{outlook_id}", tags=[Tags.outlooks])
async def read_outlook(
        outlook_id: Annotated[int, Path(title="The id of the outlook to get")],
        session: SessionDep
        ):
    outlook = session.get(Outlook, outlook_id)
    return outlook

@app.post(
        "/outlooks/",
        response_model=Outlook,
        tags=[Tags.outlooks],
        summary="Create a new outlook",
        )
async def create_outlook(outlook: Outlook, session: SessionDep) -> Outlook:
    """
    Create a outlook with all of the information:
    - TODO
    """    
    session.add(outlook)
    session.commit()
    session.refresh(outlook)
    return outlook
