from sqlmodel import Session

from app import crud
from app.models import Outlook, OutlookCreate
from test_utils.utils import random_year

def create_random_outlook (database: Session) -> Outlook:
    year = random_year()
    outlook_in = OutlookCreate(start_year=year)
    return crud.create_outlook(session=database, outlook_in=outlook_in)

