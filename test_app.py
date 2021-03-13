from app import create_app
from models import Movie

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


def test_get_movies_default_page():
    response = client().get('/movies')
    assert response.status_code == 200

    movies = [m.format() for m in Movie.query.order_by(Movie.id).slice(0, 10)]
    total_movies = Movie.query.count()

    data = response.get_json()
    assert data['success']
    assert data['movies'] == movies
    assert data['total_movies'] == total_movies
