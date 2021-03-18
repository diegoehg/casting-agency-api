import pytest
from app import create_app
from models import db, Movie
from data_loader import load_data


@pytest.fixture(scope='module')
def client():
    database_dialect = "postgresql"
    database_user = "casting_tester"
    database_password = "testinguser"
    database_location = "localhost:5432"
    database_name = "casting_agency_test"

    test_config = {
        'DATABASE_URL': f"{database_dialect}://{database_user}:{database_password}@{database_location}/{database_name}"
    }

    app = create_app(test_config)
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
            load_data()
            yield testing_client


def get_authorization_header(token):
    return {
        'Authorization': f'Bearer {token}'
    }


@pytest.fixture(scope='module')
def token_casting_assistant():
    yield get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMGRmNmI2ZmZjYmUyMDA2YTg4NmUyZCIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2MDMzNzIzLCJleHAiOjE2MTYwNDA5MjMsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.chIxG2SEouVdBMKNS6WeS4f3o6R_OVuFqjbPnog7soan07mX2x753gcefEqRryx1WX3uXU6fQd3B5aya4iMFmSWmIMXpAeSVZ8rsm9fCOR1oRrye6778xXZlH1o4RVUvAAU-sLKbVuvtaHVGWhrONYVxxnNVBLzenJf6gR2iArUUfloG2cUJ4aykj5g609LasHHXWM8kJxQFa7KNuDNCyrWe7CsdR-8RDXqyO643NgpF8okbP7ygr7z-01Hv16E-hnsAh1CzzBHvaoFF8zOahGhSQQ_9vNkdAl0-u39DHpFPdNakZDG45vZ5UZoGZdP3_wOLIr2lDOwf-cYIY-evKQ")


@pytest.fixture(scope='module')
def token_casting_director():
    yield get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNTJiMmQ1ODQzNWRhMDA2ODg0ODI2OSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2MDM2Mzk2LCJleHAiOjE2MTYwNDM1OTYsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.sPGA9B1C-8K51FfeSl48Guwf7eRGEjCxSl_LUBiuBw_RlA33Ls346VWTmUg0NmVR71RVqHcWS0HbjnISFUr9LHWcTbSXRn-5IitrYp2CcHhGvSJpD_UH1zAOZGRWrRxo63-gI_7ws1f3qbXCgqdc0HWdCvcZpDYvEoYFTZfy8yVdPtbWRqZQhUenL9sAKEJmCRLALH_OGO6SWBB5OyZcyyDswJT26hQjIaBG5Y-ECuSf8pPrOMRZI9GfPCKGoGNmk93EixOOz44uS1hcLY4tzLJY1SR-Seuw5sXdhFLZYjGdmXGeigGLkq3fcMXahMjzdeWB_exJY5tfOm4iRgFlGQ")


@pytest.fixture(scope='module')
def token_executive_producer():
    yield get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNTJiNDY2MjYyNjFhMDA2ZmE5MGJhOSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2MDM2NzY2LCJleHAiOjE2MTYwNDM5NjYsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.ESjKGwdKL2idPjdPFlYDIKBAxrBsqlji52aNOprVsojxYOcg5wbJjmcBOJhytTA8qdcWSZonQNU2SNBvu2ahYWbf2EPVr8OC0nFHph9QLmXvDQeccwybjxuwyytoP5koaHdVbv4sE7kXoJCNaBU9-kOCyv5w7E2QxR00kIDdXohECMQiv1eQfcTnJXC5pYuNJpJYgMogMYbrUozr057giAKmaONdjowSZviQYy24ju7jXEJebXRLgioy-I48F2vzmSszFg-wn84IAo6hKEiKqiUHjsHTfiCyHH3mNqXZuLf1thkVg1vZvbkat856w1mQC6sxCNDELU-PBl65yj2xMQ")


def test_get_movies_default_page(client, token_casting_assistant):
    response = client.get('/movies',
                          headers=token_casting_assistant)
    assert response.status_code == 200

    movies = [m.format() for m in Movie.query.order_by(Movie.id).slice(0, 10)]
    total_movies = Movie.query.count()

    data = response.get_json()
    assert data['success']
    assert data['movies'] == movies
    assert len(data['movies']) == 10
    assert data['total_movies'] == total_movies


def test_get_movies_page_2(client, token_casting_assistant):
    response = client.get('/movies',
                          query_string={'page': 2},
                          headers=token_casting_assistant)
    assert response.status_code == 200

    movies = [m.format() for m in Movie.query.order_by(Movie.id).slice(10, 20)]
    total_movies = Movie.query.count()

    data = response.get_json()
    assert data['success']
    assert data['movies'] == movies
    assert len(data['movies']) == 10
    assert data['total_movies'] == total_movies


def test_404_in_get_movies_unexistent_page(client, token_casting_assistant):
    response = client.get('/movies',
                          query_string={'page': 2000},
                          headers=token_casting_assistant)
    assert response.status_code == 404

    data = response.get_json()
    assert not data['success']
    assert data['error'] == 404
    assert data['message'] == 'Resource not found'


def test_get_movies_with_casting_assistant_token(client, token_casting_assistant):
    response = client.get('/movies',
                          headers=token_casting_assistant)
    assert response.status_code == 200


def test_get_movies_with_casting_director_token(client, token_casting_director):
    response = client.get('/movies',
                          headers=token_casting_director)
    assert response.status_code == 200


def test_get_movies_with_executive_producer_token(client, token_executive_producer):
    response = client.get('/movies',
                          headers=token_executive_producer)
    assert response.status_code == 200


def test_401_when_request_does_not_contain_authorization_header(client):
    response = client.get('/movies')
    assert response.status_code == 401

    data = response.get_json()
    assert not data['success']
    assert data['error'] == 401
    assert data['message'] == 'Request does not contain authorization header'


def test_401_when_authorization_header_doesnt_start_with_bearer(client):
    response = client.get('/movies', headers={'Authorization': 'Aaaa Token'})
    assert response.status_code == 401

    data = response.get_json()
    assert not data['success']
    assert data['error'] == 401
    assert data['message'] == 'Authorization header must start with Bearer'


def test_401_when_authorization_header_has_no_token(client):
    response = client.get('/movies', headers={'Authorization': 'Bearer'})
    assert response.status_code == 401

    data = response.get_json()
    assert not data['success']
    assert data['error'] == 401
    assert data['message'] == 'Authorization header has no token'


def test_401_when_authorization_header_is_malformed(client):
    response = client.get('/movies', headers={'Authorization': 'Bearer 983495834 data'})
    assert response.status_code == 401

    data = response.get_json()
    assert not data['success']
    assert data['error'] == 401
    assert data['message'] == 'Authorization header must be bearer token'


if __name__ == "__main__":
    pytest.main()
