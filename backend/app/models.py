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

# Shared
class VisionBase(SQLModel):
    title: str = Field(default="Aspirational Vision", min_length=1, max_length=200)
    description: str | None = Field (
            default= None, title="Vision Description", max_length=300
            )
# Properties to receive on vision creation
class VisionCreate(VisionBase):
    pass

# Database model, table inferred from class name
class Vision(VisionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

# returned via API, id always required
class VisionPublic(VisionBase):
    id: int

class VisionsPublic(SQLModel):
    data: list[VisionPublic]
    count: int

# ========= Outlook Layer ========= 

# Shared
class OutlookBase(SQLModel):
    start_year: int = Field(gt=0, description="The year that your current Three Year Outlook began.")

# Properties to receive on outlook creation
class OutlookCreate(OutlookBase):
    pass

# Database model, table inferred from class name
class Outlook(OutlookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

# returned via API, id always required
class OutlookPublic(OutlookBase):
    id: int

class OutlooksPublic(SQLModel):
    data: list[OutlookPublic]
    count: int
