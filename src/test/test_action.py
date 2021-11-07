from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_action_1():
    text = "哈囉, Phoebe"
    response = client.post("/action/",
                           json={"text": text})
    assert response.status_code == 200
    assert response.json() == {"action": "揮手", "text": "Hello, {username}"}