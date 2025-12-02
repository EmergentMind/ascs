from fastapi.testclient import TestClient
from sqlmodel import Session

from tests.utils.outlook import create_random_outlook

def test_create_outlook(
        client: TestClient,) -> None:
    data = {"start_year": 2025}
    response = client.post(
            f"/outlooks/",
            json=data,
            )
    content = response.json()
    assert content["start_year"] == data["start_year"]
    assert "id" in content

def test_read_outlook(
        client: TestClient,
        database: Session,
        ) -> None:
    outlook = create_random_outlook(database)
    response = client.get(
            f"/outlooks/{outlook.id}",
            )
    content = response.json()
    assert content["start_year"] == outlook.start_year

