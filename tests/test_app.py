from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")

    texto = response.data.decode('utf-8')

    assert response.status_code == 200
    assert "Aula 4" in texto

