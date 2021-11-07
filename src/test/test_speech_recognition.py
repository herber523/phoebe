from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_sst_1():
    response = client.post("/speech_recognition/",
                           files={"file": ("filename", open('./files/test_stt_file_1.mp3', "rb"), "image/jpeg")})
    assert response.status_code == 200
    assert response.json() == {"text": "哈囉, Phoebe", "action": {"action": "揮手", "text": "Hello, {username}"}}


def test_sst_2():
    response = client.post("/speech_recognition/",
                           files={"file": ("filename", open('./files/test_stt_file_2.mp3', "rb"), "image/jpeg")})
    assert response.status_code == 200
    assert response.json() == {"text": "看起來不太好吃 我媽以前", "action": {"action": "靜止", "text": ""}}


def test_sst_3():
    response = client.post("/speech_recognition/",
                           files={"file": ("filename", open('./files/test_stt_file_3.mp3', "rb"), "image/jpeg")})
    assert response.status_code == 200
    assert response.json() == {"text": "Phoebe 人死了之後 到底去哪裡", "action": {"action": "說話", "text": "墳墓 一般都是火葬，現在沒有人土葬"}}
