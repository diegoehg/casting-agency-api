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
    yield get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMGRmNmI2ZmZjYmUyMDA2YTg4NmUyZCIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2MTI1NzY0LCJleHAiOjE2MTYxMzI5NjQsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.QVDBcxebWftb9-MMvwXw7PIQYOeB6Hrw14fJPPce-YoRk7cpvPEwvPB_DzzOrIOUS36vHfyKDYYp2KIFlfe13tEDNfu3m-2lLiAOjmSXlNXToi_snU-Kt1k_vccLRldzGVK5FF6BqiuznBYJI-Wn87tP16CSPfY_REveHLQv9NAHIFJ7agFfOOxt2mdJe5QtETlbfhr8r_-Nx0hwLRfPfjTzzM0k-MTDaBkcOrTieWUoT7C8LIulMV6j8RuuVB0ptQML4yiMIJVyQ3kfmEV_UAThcsZG3tWGoGbuj811nBM1bpbMq26rwD6mILhqKoQIIviKzCD7ClbTslMuH1LRjg")


@pytest.fixture(scope='module')
def token_casting_director():
    yield get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNTJiMmQ1ODQzNWRhMDA2ODg0ODI2OSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2MTI1ODczLCJleHAiOjE2MTYxMzMwNzMsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.m8Gi2KQlabokPTOtCUqzeSIpzXcv87iebqxiuEj4a70L-nhcLQRINlozO9aasfWqfBZKtQiVxrkswQZ-cNUjn0N3Bq9WkMKhq9ta8JRv9ZxwP5m214-NiuAGKj2_D9HvkQqH8_3AbE80bWIl7c9_h9zkAI8q88QOryFrQD04Q3tOHr420Z8r8f3iL-wqFksYV0WJJ2wkdH0H0ZfyrI_O7THr62CmWvrucukd2fwX9tR0fr1i2FwnSzylHh81vzO7lG7RLC3crsCKBgjeoqChcIgnmshEkwyV6pOkl60cSzozC5oie2aCloJ2Dxy95U3943LNTw-2pSrTN_GCle4mdA")


@pytest.fixture(scope='module')
def token_executive_producer():
    yield get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNTJiNDY2MjYyNjFhMDA2ZmE5MGJhOSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2MTI1OTY2LCJleHAiOjE2MTYxMzMxNjYsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.iylxqtJkVYtLdIE7cnm8OFv3qdEl1nBzBIIkdoYTLfNZ45mrylduUEV2_DFOtfKGXE0mSems20AWSbUYSdFC2Bv5p4tokKjhxnPcgb7BuOe0Btk8gpmTzwkucdb6LIprri0XnjaDwMYjrByoyNWRbSP_dZRpx3d6AUeoO5ENimKJ56aAQG-xbFU3aidc_bEjEyeYfMJuAitsi0TPk-V49QuE7zp12dIe-A5Kb6kFKXPBfvjx3RFqUMXQPppwfBmBXkIy-c1ys7aZzY1AGyzGjucxOLuik17mW5sF9Gjb5gvd2IIxU3OOW2tHB9K6A5eusPgnGooi-EOf7GnxK0yPSA")


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
