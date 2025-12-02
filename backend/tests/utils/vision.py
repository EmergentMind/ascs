from sqlmodel import Session

from app import crud
from app.models import Vision, VisionCreate
from tests.utils.utils import random_lower_string

def create_random_vision(database: Session) -> Vision:
    title = random_lower_string()
    description = random_lower_string()
    vision_in = VisionCreate(title=title, description=description)
    return crud.create_vision(session=database, vision_in=vision_in)

