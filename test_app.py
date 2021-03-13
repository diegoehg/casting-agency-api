from app import create_app

database_dialect = "postgresql"
database_user = "casting_tester"
database_password = "testinguser"
database_location = "localhost:5432"
database_name = "casting_agency_test"

test_config = {
    'DATABASE_URL': f"{database_dialect}://{database_user}:{database_password}@{database_location}/{database_name}"
}

app = create_app(test_config)
client = app.test_client


def test_get_movies():
    response = client().get('/movies')
    assert response.status_code == 200

    data = response.get_json()
    assert data['success']
