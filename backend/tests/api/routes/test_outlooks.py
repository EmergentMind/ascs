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

    assert response.status_code == 200
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

    assert response.status_code == 200
    content = response.json()
    assert content["start_year"] == outlook.start_year

def test_read_outlook_not_found(
        client: TestClient,
        ) -> None:
    #NOTE: we can replace this when we use UUIDs for id
    non_existent_id = 999999
    response = client.get(
            f"/outlooks/{non_existent_id}",
            )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Item not found"

