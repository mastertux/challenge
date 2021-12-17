import random
from fastapi.testclient import TestClient


def test_read_segment(client: TestClient):
    r = client.get("/api/v1/segments")
    assert r.status_code == 200


def test_create_segment(client: TestClient):
    rdata = random.randrange(1, 1000)
    data = {"name": f"Teste {rdata}"}
    r = client.post("/api/v1/segments/", json=data)
    assert r.status_code == 201
