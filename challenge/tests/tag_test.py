from fastapi.testclient import TestClient
import random


def test_read_tag(client: TestClient):
    r = client.get("/api/v1/tags")
    assert r.status_code == 200


def test_create_tag(client: TestClient):
    rdata = random.randrange(1, 1000)
    data = {"name": f"Teste {rdata}"}
    r = client.post("/api/v1/tags/", json=data)
    assert r.status_code == 201
