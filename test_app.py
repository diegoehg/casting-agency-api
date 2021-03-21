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


token_header = {
    "casting_assistant": get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMGRmNmI2ZmZjYmUyMDA2YTg4NmUyZCIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2Mjk4Mjk3LCJleHAiOjE2MTYzODQ2OTcsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.fbsAzhFnT3gJklblW_RnHBR7kjHrAr2ULNShe4WNjCo-FfOX-1638HA9POIy989mNN7ipi-wB86LVU8bn8-CzWDl9KdH_Udtc0aXgGNdExYqmYMkOxXKzzL3RngxRxK1oViwan9AJsz4H5jjkHnPhOb6IOoveEyo-N5WEkYJxa-lUNtOoMUogFlbrKz9Xao_4PDNu1lTXf4wbc0wTMyn6gjaBtkgQjYT9MS4C-QK0b_gllhxzwpdgt0-Q4na0OeZzTVRBXHi2vhJN9EgvaGwaj29FQY8QUu5JEIkg64BJd1kKFvPk12uNCqsOPezsLFcKZi4NsLP_Up7HFeWzeioxg"),
    "casting_director": get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNTJiMmQ1ODQzNWRhMDA2ODg0ODI2OSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2Mjk4MzQzLCJleHAiOjE2MTYzODQ3NDMsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.TmY81xJb6FY_uqMA_g3zzp2mvJUbNZMGk-n6tuCj7kGq1YuJNObIFSeVn3Y8X7FN59baM9SiJll3lqDz15j9s7RFCzYh4VqB1seLGuncD7C71EWXvkZ1sOnuAPESpAozP8hEJoFAg_xOvKZh0xHif1XugBVqoc6yr9n9aHZr8YI-9xSy8YLeuvkI_mRguHDLGQo-gpmBATGWj-Si2Z3YMtkf6KVPt_i8iPq317Phr7UbRvk_laj9d4w2J-FhwXK3LnThbTFDBKf7HIE7p5RGhdx3dAiBIJ_y3Xdz75fEQ6RaRkkENtQBGzeM5YBFYBJfZUU3pL5DKRUDEoMSx5kiLw"),
    "executive_producer": get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNTJiNDY2MjYyNjFhMDA2ZmE5MGJhOSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2Mjk4Mzg5LCJleHAiOjE2MTYzODQ3ODksImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.Ml9SRlhddC_TyGkh0yStRFSLHi3QoqX2eeo2pCAWt46mMEsH_2HR0n3Mfvx-GOV_bxACQrr6MeE5diORm8nOXLr_tzaRToa_Vy0vHb8B6ah50A8_mr48tiaYYaHS4y49u5Dpx8lwH9mIamEIKHu5FKVdDXEieJu4W1j3qj6EgORa0BTVC2KyAo0-vncSsVot3SAz9p12n2sa-fUztO0uTZDZyYS7IS9U21-ywUbIolh3Ge4fcx7BfNoe_5-qcussKx19BfWKh8U5455CXskhheZZYGojzDWAI3miRtTpFevkVi8tQ_jnaG5YQmsVODciCfHhjOk_JL5RtdSJv9w5Sw")
}


@pytest.fixture(scope='module')
def token_casting_assistant():
    yield get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMGRmNmI2ZmZjYmUyMDA2YTg4NmUyZCIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2Mjk4Mjk3LCJleHAiOjE2MTYzODQ2OTcsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.fbsAzhFnT3gJklblW_RnHBR7kjHrAr2ULNShe4WNjCo-FfOX-1638HA9POIy989mNN7ipi-wB86LVU8bn8-CzWDl9KdH_Udtc0aXgGNdExYqmYMkOxXKzzL3RngxRxK1oViwan9AJsz4H5jjkHnPhOb6IOoveEyo-N5WEkYJxa-lUNtOoMUogFlbrKz9Xao_4PDNu1lTXf4wbc0wTMyn6gjaBtkgQjYT9MS4C-QK0b_gllhxzwpdgt0-Q4na0OeZzTVRBXHi2vhJN9EgvaGwaj29FQY8QUu5JEIkg64BJd1kKFvPk12uNCqsOPezsLFcKZi4NsLP_Up7HFeWzeioxg")


@pytest.fixture(scope='module')
def token_casting_director():
    yield get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNTJiMmQ1ODQzNWRhMDA2ODg0ODI2OSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2Mjk4MzQzLCJleHAiOjE2MTYzODQ3NDMsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.TmY81xJb6FY_uqMA_g3zzp2mvJUbNZMGk-n6tuCj7kGq1YuJNObIFSeVn3Y8X7FN59baM9SiJll3lqDz15j9s7RFCzYh4VqB1seLGuncD7C71EWXvkZ1sOnuAPESpAozP8hEJoFAg_xOvKZh0xHif1XugBVqoc6yr9n9aHZr8YI-9xSy8YLeuvkI_mRguHDLGQo-gpmBATGWj-Si2Z3YMtkf6KVPt_i8iPq317Phr7UbRvk_laj9d4w2J-FhwXK3LnThbTFDBKf7HIE7p5RGhdx3dAiBIJ_y3Xdz75fEQ6RaRkkENtQBGzeM5YBFYBJfZUU3pL5DKRUDEoMSx5kiLw")


@pytest.fixture(scope='module')
def token_executive_producer():
    yield get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNTJiNDY2MjYyNjFhMDA2ZmE5MGJhOSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2Mjk4Mzg5LCJleHAiOjE2MTYzODQ3ODksImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.Ml9SRlhddC_TyGkh0yStRFSLHi3QoqX2eeo2pCAWt46mMEsH_2HR0n3Mfvx-GOV_bxACQrr6MeE5diORm8nOXLr_tzaRToa_Vy0vHb8B6ah50A8_mr48tiaYYaHS4y49u5Dpx8lwH9mIamEIKHu5FKVdDXEieJu4W1j3qj6EgORa0BTVC2KyAo0-vncSsVot3SAz9p12n2sa-fUztO0uTZDZyYS7IS9U21-ywUbIolh3Ge4fcx7BfNoe_5-qcussKx19BfWKh8U5455CXskhheZZYGojzDWAI3miRtTpFevkVi8tQ_jnaG5YQmsVODciCfHhjOk_JL5RtdSJv9w5Sw")


@pytest.fixture(scope='module')
def valid_json_new_movie():
    return {
        "title": "Godzilla vs. King Kong",
        "release_date": "2021-07-23"
    }


@pytest.fixture(scope='module')
def valid_json_new_actor():
    return {
        "name": "John Brubeck",
        "age": 36,
        "gender": "male"
    }


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

    movie = data['movie']
    assert movie['id'] == m.id
    assert movie['title'] == m.title
    assert movie['release_date'] == m.release_date.isoformat()


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


def test_post_movies(client, valid_json_new_movie, token_executive_producer):
    total_movies_before_post = Movie.query.count()

    response = client.post('/movies',
                           json=valid_json_new_movie,
                           headers=token_executive_producer)
    assert response.status_code == 201

    total_movies_after_post = Movie.query.count()
    assert total_movies_before_post + 1 == total_movies_after_post

    data = response.get_json()
    assert data['success']

    movie_created = data['movie']
    assert movie_created['id'] is not None
    assert movie_created['title'] == valid_json_new_movie['title']
    assert movie_created['release_date'] == valid_json_new_movie['release_date']


def test_422_in_post_movies_invalid_fields(client, token_executive_producer):
    malformed_movie = {
        "titlle": "Fantastic Four"
    }
    response = client.post('/movies',
                           json=malformed_movie,
                           headers=token_executive_producer)
    assert response.status_code == 422

    data = response.get_json()
    assert not data['success']
    assert data['error'] == 422
    assert data['message'] == "The request was well-formed but was unable to be followed due to semantic errors"


def test_400_in_post_movies_body_malformed(client, token_executive_producer):
    response = client.post('/movies',
                           json="Malformed",
                           headers=token_executive_producer)
    assert response.status_code == 400

    data = response.get_json()
    assert not data['success']
    assert data['error'] == 400
    assert data['message'] == 'The server cannot process the request'


def test_authorized_post_movies_with_executive_producer(client,
                                                        valid_json_new_movie,
                                                        token_executive_producer):
    response = client.post('/movies',
                           json=valid_json_new_movie,
                           headers=token_executive_producer)
    assert response.status_code == 201


def test_401_post_movies_with_casting_assistant(client,
                                                valid_json_new_movie,
                                                token_casting_assistant):
    response = client.post('/movies',
                           json=valid_json_new_movie,
                           headers=token_casting_assistant)
    assert response.status_code == 401


def test_401_post_movies_with_casting_director(client,
                                               valid_json_new_movie,
                                               token_casting_director):
    response = client.post('/movies',
                           json=valid_json_new_movie,
                           headers=token_casting_director)
    assert response.status_code == 401


@pytest.mark.parametrize(
    "token, new_release_date",
    [
        (token_header['casting_director'], "2021-03-19"),
        (token_header['executive_producer'], "2022-03-19")
    ]
)
def test_patch_movie(client, token, new_release_date):
    patch_body = {
        "release_date": new_release_date
    }
    movie_before_patch = Movie.query.get(3).format()
    response = client.patch('/movies/3',
                            json=patch_body,
                            headers=token)
    assert response.status_code == 200

    data = response.get_json()
    assert data['success']

    movie_after_patch = data['movie']
    assert movie_after_patch['title'] == movie_before_patch['title']
    assert movie_after_patch['release_date'] != movie_before_patch['release_date']
    assert movie_after_patch['release_date'] == patch_body['release_date']


@pytest.mark.parametrize(
    "token",
    [token_header['casting_director'], token_header['executive_producer']]
)
def test_404_in_patch_movie_unexistent_id(client, token):
    response = client.patch('/movies/949489',
                            json={"title": "Titanic 2"},
                            headers=token)
    assert response.status_code == 404

    data = response.get_json()

    assert not data['success']
    assert data['error'] == 404
    assert data['message'] == 'Resource not found'


@pytest.mark.parametrize(
    "token",
    [token_header['casting_director'], token_header['executive_producer']]
)
def test_422_in_patch_movie_invalid_fields(client, token):
    response = client.patch('/movies/5',
                            json={"tittle": "Titanic 3"},
                            headers=token)
    assert response.status_code == 422

    data = response.get_json()
    assert not data['success']
    assert data['error'] == 422
    assert data['message'] == "The request was well-formed but was unable to be followed due to semantic errors"


@pytest.mark.parametrize(
    "token",
    [token_header['casting_director'], token_header['executive_producer']]
)
def test_400_in_patch_movie_malformed_request(client, token):
    response = client.patch('/movies/1',
                            json="Malformed request",
                            headers=token)
    assert response.status_code == 400

    data = response.get_json()
    assert not data['success']
    assert data['error'] == 400
    assert data['message'] == 'The server cannot process the request'


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


def test_get_actors_with_casting_assistant(client, token_casting_assistant):
    response = client.get('/actors',
                          headers=token_casting_assistant)
    assert response.status_code == 200


def test_get_actors_with_casting_director(client, token_casting_director):
    response = client.get('/actors',
                          headers=token_casting_director)
    assert response.status_code == 200


def test_get_actors_with_executive_producer(client, token_executive_producer):
    response = client.get('/actors',
                          headers=token_executive_producer)
    assert response.status_code == 200


def test_get_actor(client, token_casting_assistant):
    response = client.get('/actors/1',
                          headers=token_casting_assistant)
    assert response.status_code == 200

    a = Actor.query.get(1)
    data = response.get_json()

    assert data['success']

    actor = data['actor']
    assert actor['id'] == a.id
    assert actor['name'] == a.name
    assert actor['age'] == a.age
    assert actor['gender'] == a.gender.value


def test_404_when_get_actor_unexistent_id(client, token_casting_assistant):
    response = client.get('/actors/9000',
                          headers=token_casting_assistant)
    assert response.status_code == 404

    data = response.get_json()

    assert not data['success']
    assert data['error'] == 404
    assert data['message'] == 'Resource not found'


def test_get_actor_with_casting_assistant(client, token_casting_assistant):
    response = client.get('/actors/1',
                          headers=token_casting_assistant)
    assert response.status_code == 200


def test_get_actor_with_casting_director(client, token_casting_director):
    response = client.get('/actors/1',
                          headers=token_casting_director)
    assert response.status_code == 200


def test_get_actor_with_executive_producer(client, token_executive_producer):
    response = client.get('/actors/1',
                          headers=token_executive_producer)
    assert response.status_code == 200


def test_post_actors(client, valid_json_new_actor, token_casting_director):
    total_actors_before_post = Actor.query.count()

    response = client.post('/actors',
                           json=valid_json_new_actor,
                           headers=token_casting_director)
    assert response.status_code == 201

    total_actors_after_post = Actor.query.count()
    assert total_actors_before_post+1 == total_actors_after_post

    data = response.get_json()
    assert data['success']

    actor_created = data['actor']
    assert actor_created['id'] is not None
    assert actor_created['name'] == valid_json_new_actor['name']
    assert actor_created['age'] == valid_json_new_actor['age']
    assert actor_created['gender'] == valid_json_new_actor['gender']


def test_422_in_post_actors_invalid_fields(client, token_casting_director):
    malformed_actor = {
        "name": "Fantastic Four",
        "aaage": 74
    }
    response = client.post('/actors',
                           json=malformed_actor,
                           headers=token_casting_director)
    assert response.status_code == 422

    data = response.get_json()
    assert not data['success']
    assert data['error'] == 422
    assert data['message'] == "The request was well-formed but was unable to be followed due to semantic errors"


def test_400_in_post_actors_body_malformed(client, token_casting_director):
    response = client.post('/actors',
                           json="request body malformed",
                           headers=token_casting_director)
    assert response.status_code == 400

    data = response.get_json()
    assert not data['success']
    assert data['error'] == 400
    assert data['message'] == 'The server cannot process the request'


def test_authorized_post_actors_with_casting_director(client,
                                                      valid_json_new_actor,
                                                      token_casting_director):
    response = client.post('/actors',
                           json=valid_json_new_actor,
                           headers=token_casting_director)
    assert response.status_code == 201


def test_authorized_post_actors_with_executive_producer(client,
                                                        valid_json_new_actor,
                                                        token_executive_producer):
    response = client.post('/actors',
                           json=valid_json_new_actor,
                           headers=token_executive_producer)
    assert response.status_code == 201


def test_401_post_actors_with_casting_assistant(client,
                                                valid_json_new_actor,
                                                token_casting_assistant):
    response = client.post('/actors',
                           json=valid_json_new_actor,
                           headers=token_casting_assistant)
    assert response.status_code == 401


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
