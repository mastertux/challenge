from fastapi.testclient import TestClient
import random


def test_read_user(client: TestClient):
    r = client.get("/api/v1/users")
    assert r.status_code == 200


def test_create_user(client: TestClient):
    rdata = random.randrange(1, 1000)
    data = {
        "first_name": f"Teste {rdata}",
        "last_name": f"last name {rdata}",
        "email": f"teste{rdata}@teste.com",
        "sex": "male",
        "birth_date": "2020-01-01",
        "admission_date": "2020-01-01",
        "is_active": True,
        "segment_id": 1,
        "tags": [
            2
        ]
    }

    r = client.post("/api/v1/users/", json=data)
    assert r.status_code == 201
