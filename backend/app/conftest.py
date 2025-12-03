from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, delete

from app.core.database import engine, init_database 
from app.main import app
from app.models import Vision, Outlook

@pytest.fixture(scope="session", autouse=True)
def database() -> Generator[Session, None, None]:
    with Session(engine) as session:
        init_database()
        yield session
        statement = delete(Vision)
        session.exec(statement)
        statement = delete(Outlook)
        session.exec(statement)
        session.commit()

@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as client:
        yield client

