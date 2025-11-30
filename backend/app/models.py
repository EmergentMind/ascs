from sqlmodel import Field, SQLModel
from typing import Optional

from enum import Enum

# ========= Common ========= 

class Tags(Enum):
    visions = "visions"
    outlooks = "outlooks"
    seasons = "seasons"
    users = "users"

# ========= Vision Layer ========= 

class Vision(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(default="Aspirational Vision")
    description: str | None = Field (
            default= None, title="Vision Description", max_length=300
            )

# ========= Outlook Layer ========= 

class Outlook(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    start_year: int = Field(gt=0, description="The year that your current Three Year Outlook began.")
