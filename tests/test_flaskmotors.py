def test_app_is_created(app):  # injeção de depêndencia
    assert app.name == "flaskmotors.app"


def test_request_returns_200(client):
    assert client.get("/api/v1/pessoas").status_code == 200


def test_request_returns_content_type(client):
    assert client.get("/api/v1/pessoas").content_type == "application/json"


# def test_real_request(live_server):
#     ...
