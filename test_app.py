import pytest
from app import create_app
from models import db, Movie, Actor
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
    yield get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMGRmNmI2ZmZjYmUyMDA2YTg4NmUyZCIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2MjEwOTg1LCJleHAiOjE2MTYyOTczODUsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.p7AQ9JNDQXPlWBL6PbUgXhv7ciEfgSGl-QCWEf-JjJwdfgjZ-wN2jRXGFHbfyq4CaoRP0Ht5c25nZUwO3XCYylIRB80WzOSJ2yReKbJMILM_LStczlCi21EGj_AEJJxK0JqurmjjUmFJQF8hLbsnkVKY2cSiFPW1R_y46rTejujxGRihrmBJOr72fo1G0FgTCPCTm-Ae5uTaY2ELyykI3Q3Q52HVpSwXSE4Zm7PtwldwrDK3KnG4XUg8L-y3B1NNpzXVFMySXXuIRUYwTfnpNu5i3CnQ1gW5g41WlpKqzAAMdQqUSkgXYyKBLtPbE5YDtxrevHf7DW4kMZmFECn6kw")


@pytest.fixture(scope='module')
def token_casting_director():
    yield get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNTJiMmQ1ODQzNWRhMDA2ODg0ODI2OSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2MjExMDYzLCJleHAiOjE2MTYyOTc0NjMsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.UpeHYagUq3Cw3gdm0QhY66G9yZQwz6T9QCkSnFh6VAU1W-8vOvJ-yt_PlIWv0NczTAwmVYmokBOOO77OWW1A3mULeexxsVrIzQRe0IEt1Jc3VPgEG4A5vcGU9999B1JTaKFKAzW-ybgVg1euiMBT_oTEfy0rLFb2-8Q7u47qP7_Jp6FPrvLCsSHzTFChjAEZu7zkV6z353uLr7D1qQ_rXn382gDr9nI8J1NkmaPynaWxf84hy129jTrq9Zouc2Ng-sZGpGdVaoWvI7qWsJI_SX3u0EQpX4fBc3nBPY6yGpWbgDSLS2H828N7ljSlpQQ1TipDX9fOJU0PGe1MuIA17w")


@pytest.fixture(scope='module')
def token_executive_producer():
    yield get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNTJiNDY2MjYyNjFhMDA2ZmE5MGJhOSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2MjExMTE0LCJleHAiOjE2MTYyOTc1MTQsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.NXU80E4esWCP0snSFKFh5850h_Oq6GhTSwHwdIXhaFMk4zfZ9II_mr69eVkrxtJBgH7P962iVc-MvX0vWYRuVV2NF6-bYUCzfmPuQEToD92yy89Wjm5J9DqCI5LjRvqYW1kiT7oICfJkLS2aKJlvDVkoqKRhAHXPklOtSOTjaNxWrvSEbIPC8t3SRHEelXc4CIBRUWPxEKcoOQbmvrgTUvzXB_PeS8j8DG_gfmmsKgCc85IJcUD-t0p1xLBtyvDN1EPKmTej83H8hx38zS8JvcfH4-WjpOfyBnDe0ccssF6s9g7rJwZa-IYpF2xWCSrHDEGcqQBWtzfmM-_2ligFTw")


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


def test_get_movie(client, token_casting_assistant):
    response = client.get('/movies/1',
                          headers=token_casting_assistant)
    assert response.status_code == 200

    m = Movie.query.get(1)

    data = response.get_json()
    assert data['success']
    assert data['id'] == m.id
    assert data['title'] == m.title
    assert data['release_date'] == m.release_date.isoformat()


def test_404_when_get_movie_unexistent_id(client, token_casting_assistant):
    response = client.get('/movies/8484958',
                          headers=token_casting_assistant)
    assert response.status_code == 404

    data = response.get_json()
    assert not data['success']
    assert data['error'] == 404
    assert data['message'] == 'Resource not found'


def test_get_movie_with_casting_assistant_token(client, token_casting_assistant):
    response = client.get('/movies/1',
                          headers=token_casting_assistant)
    assert response.status_code == 200


def test_get_movie_with_casting_director_token(client, token_casting_director):
    response = client.get('/movies/1',
                          headers=token_casting_director)
    assert response.status_code == 200


def test_get_movie_with_executive_producer_token(client, token_executive_producer):
    response = client.get('/movies/1',
                          headers=token_executive_producer)
    assert response.status_code == 200


def test_get_actors_default_page(client, token_casting_assistant):
    response = client.get('/actors',
                          headers=token_casting_assistant)
    assert response.status_code == 200

    actors = [a.format() for a in Actor.query.order_by(Actor.id).slice(0, 10)]
    total_actors = Actor.query.count()

    data = response.get_json()

    assert data['success']
    assert data['actors'] == actors
    assert data['total_actors'] == total_actors


def test_get_actors_second_page(client, token_casting_assistant):
    response = client.get('/actors',
                          query_string={'page': 2},
                          headers=token_casting_assistant)
    assert response.status_code == 200

    actors = [a.format() for a in Actor.query.order_by(Actor.id).slice(10, 20)]
    total_actors = Actor.query.count()

    data = response.get_json()

    assert data['success']
    assert data['actors'] == actors
    assert data['total_actors'] == total_actors


def test_404_if_get_actors_unexistent_page(client, token_casting_assistant):
    response = client.get('/actors',
                          query_string={'page': 2009},
                          headers=token_casting_assistant)
    assert response.status_code == 404

    data = response.get_json()

    assert not data['success']
    assert data['error'] == 404
    assert data['message'] == 'Resource not found'


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
