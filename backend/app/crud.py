from sqlmodel import Session
from app.models import Vision, VisionCreate, Outlook, OutlookCreate

def create_vision(*, session: Session, vision_in: VisionCreate) -> Vision:
    database_vision = Vision.model_validate(vision_in);
    session.add(database_vision)
    session.commit()
    session.refresh(database_vision)
    return database_vision

def create_outlook(*, session: Session, outlook_in: OutlookCreate) -> Outlook:
    database_outlook = Outlook.model_validate(outlook_in);
    session.add(database_outlook)
    session.commit()
    session.refresh(database_outlook)
    return database_outlook
