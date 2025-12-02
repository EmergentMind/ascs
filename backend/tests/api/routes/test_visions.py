from fastapi.testclient import TestClient
from sqlmodel import Session

from tests.utils.vision import create_random_vision

def test_create_vision(
        client: TestClient,) -> None:
    data = {"title": "Foo", "description": "Bar"}
    response = client.post(
            f"/visions/",
            json=data,
            )
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content

def test_read_vision(
        client: TestClient,
        database: Session,
        ) -> None:
    vision = create_random_vision(database)
    response = client.get(
            f"/visions/{vision.id}",
            )
    content = response.json()
    assert content["title"] == vision.title
    assert content["description"] == vision.description

def test_read_vision_not_found(
        client: TestClient,
        ) -> None:
    non_existent_id = 999999
    response = client.get(
            f"/visions/{non_existent_id}",
            )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Item not found"

