from fastapi import FastAPI, Path, Form

from sqlmodel import Field, SQLModel
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
class ThreeYearOutlook(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    start_year: int = Field(gt=0, description="The year that your current Three Year Outlook began.")
    notes: str | None = Field (
            default= None, title="Notes", max_length=300
            )

app = FastAPI()

temp_vision_db = [
        {
            "vision_id": 1,
            "title": "Bob's Vision",
            "description": "My vision for persueing my dreams" 
            }, 
        {
            "vision_id": 2,
            "title": "Alice's Vision",
            "description":"My vision for being a great mother and spouse"
            }
        ]

temp_outlook_db = [
        {
            "outlook_id": 1,
            "start_year": 2025,
            "notes": "Read War and Peace"
            },
        {
            "outlook_id": 2,
            "start_year": 2023,
            "notes": "build shed"
            }       
        ]


# vision
@app.get("/visions", tags=[Tags.visions])
async def read_visions():
    return temp_vision_db

@app.get("/visions/{vision_id}", tags=[Tags.visions])
async def read_vision(vision_id: Annotated[int, Path(title="The id of the vision to get")]):
    return temp_vision_db[vision_id]

@app.post(
        "/visions/",
        response_model=Vision,
        tags=[Tags.visions],
        summary="Create a new vision",
        )
async def create_vision(vision: Vision) -> Vision:
    """
    Create a vision with all of the information:
    - TODO
    """    
    return vision

# three year outlook
@app.get("/outlooks", tags=[Tags.outlooks])
async def read_three_year_outlooks():
    return temp_outlook_db

@app.get("/outlooks/{outlook_id}", tags=[Tags.outlooks])
async def read_three_year_outlook(outlook_id: int):
    return temp_outlook_db[outlook_id]

@app.post(
        "/outlooks/",
        response_model=ThreeYearOutlook,
        tags=[Tags.outlooks],
        summary="Create a new three year outlook",
        )
async def create_outlook(outlook: ThreeYearOutlook) -> ThreeYearOutlook:
    """
    Create a three year outlook with all of the information:
    - TODO
    """
    return outlook

