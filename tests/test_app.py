from app import app


def test_index():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Flask is running on Porter"}


def test_healthz():
    response = app.test_client().get("/healthz")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
