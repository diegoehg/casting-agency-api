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


@pytest.fixture(scope='module')
def token_header():
    def get_authorization_header(token):
        return {
            'Authorization': f'Bearer {token}'
        }

    return {
        "casting_assistant": get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMGRmNmI2ZmZjYmUyMDA2YTg4NmUyZCIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2NDk4NzM3LCJleHAiOjE2MTY1ODUxMzcsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.YsYvZeKjOMN5Ko9rVLTlfgBFofVNf8itrv8EXZ_Dq0f7-BSzE9RNWCe2skLVDgUWyjMMFZmAh1P0MKJBo1LCpdXna1wVbgk_Xk5ZwKCQoSl78spKuDbnREcWg8yNJkMi5w3balsVeWe0JmNcX-ZP0Wcmc-10shQ5o4cZn2phRGqfPfdbTQ3X2LThHMqQfW5QhqaYa5ka2waT9NbmmXRcAnxA0sW-fQek9-azCQtgd6YJDRManVgk2kXcy1ZzLRmhaPL6eRb5mFcMKoWv-e8KzneBuPQEeLWW8BVDE_pu8JRKCCNecP7rsAsLvWOX0vezbUejkd49zEg6MpAZ5ioa0Q"),
        "casting_director": get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNTJiMmQ1ODQzNWRhMDA2ODg0ODI2OSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2NDk4ODA3LCJleHAiOjE2MTY1ODUyMDcsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.WxhvhNZkdiyK_6QS05AMrUDCABY8VhDzvitq9UcmqRgK0l73EaIRyDMksOWTEj5Q-wMjogkVWMqDa1CaC3z-oCLq8ccq2J9IK39BTKffxcaEtUwa3qEKLaNUFiBcXusmTlBNwDwn9PsruJeFs2WKvgpq9GAU6kx8Q-tsPPawBRu4-4Bap7v5d_jDslRDpHlKzMWuGkegkPg0AfDVm3D_PIHPiQBCRFdK4XoKoFw8jjHlhTTZdTioX7XMLevINcOT_8a_ObA3K1VCSsi_oJbpqQa8-euHvM7rbo6Csvej5Rg9soxcmfG7bXvmWuL8O_Dm86P7FcwGcCHwZjKPkV_UBQ"),
        "executive_producer": get_authorization_header("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNTJiNDY2MjYyNjFhMDA2ZmE5MGJhOSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2NDk4ODYwLCJleHAiOjE2MTY1ODUyNjAsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.In8sjdeD89UWz1R1JFsjxTMtH0777L6ZGmgmV3zCWbLvJAkwoo05-ERkKmJca53Soi4-m_tk90ject9clUGegoyb9CftyAaWD8cay91xqwrW9mzMx3pGOnKjxCqCC49YerwmfFAL0LwyzNLDAyV_tFNgTBkI8g6aQBLn1j6j5vLsbT69MB-_NHjj4wcLW0j00j9Sp8yw_XlJVI2IzoOk02KEsgh6y5rWNeXy0JxhopnWTLkPfFbANbUIYbTI2uSzfpb0-B-2zfszJ5BfovPjaXMiWD6M-KE5pQT9302kGUwqMCXLr2ZsneGLCEOov4OFs1I1V_SoWj2a4LQD1OSRWA")
    }


def verifies_400_response(response):
    assert response.status_code == 400

    data = response.get_json()
    assert not data['success']
    assert data['error'] == 400
    assert data['message'] == 'The server cannot process the request'


def verifies_401_lack_of_permissions(response):
    assert response.status_code == 401

    data = response.get_json()
    assert not data['success']
    assert data['error'] == 401
    assert data['message'] == 'Permission not found in JWT'


def verifies_404_response(response):
    assert response.status_code == 404

    data = response.get_json()
    assert not data['success']
    assert data['error'] == 404
    assert data['message'] == 'Resource not found'


def verifies_422_response(response):
    assert response.status_code == 422

    data = response.get_json()
    assert not data['success']
    assert data['error'] == 422
    assert data['message'] == "The request was well-formed but was unable to be followed due to semantic errors"


@pytest.mark.parametrize(
    "role",
    ['casting_assistant', 'casting_director', 'executive_producer']
)
def test_get_movies_default_page(client, token_header, role):
    response = client.get('/movies',
                          headers=token_header[role])
    assert response.status_code == 200

    movies = [m.format() for m in Movie.query.order_by(Movie.id).slice(0, 10)]
    total_movies = Movie.query.count()

    data = response.get_json()
    assert data['success']
    assert data['movies'] == movies
    assert len(data['movies']) == 10
    assert data['total_movies'] == total_movies


@pytest.mark.parametrize(
    "role",
    ['casting_assistant', 'casting_director', 'executive_producer']
)
def test_get_movies_page_2(client, token_header, role):
    response = client.get('/movies',
                          query_string={'page': 2},
                          headers=token_header[role])
    assert response.status_code == 200

    movies = [m.format() for m in Movie.query.order_by(Movie.id).slice(10, 20)]
    total_movies = Movie.query.count()

    data = response.get_json()
    assert data['success']
    assert data['movies'] == movies
    assert len(data['movies']) == 10
    assert data['total_movies'] == total_movies


@pytest.mark.parametrize(
    "role",
    ['casting_assistant', 'casting_director', 'executive_producer']
)
def test_404_in_get_movies_unexistent_page(client, token_header, role):
    response = client.get('/movies',
                          query_string={'page': 2000},
                          headers=token_header[role])
    verifies_404_response(response)


@pytest.mark.parametrize(
    "role",
    ['casting_assistant', 'casting_director', 'executive_producer']
)
def test_get_movie(client, token_header, role):
    response = client.get('/movies/1',
                          headers=token_header[role])
    assert response.status_code == 200

    m = Movie.query.get(1)

    data = response.get_json()
    assert data['success']

    movie = data['movie']
    assert movie['id'] == m.id
    assert movie['title'] == m.title
    assert movie['release_date'] == m.release_date.isoformat()


@pytest.mark.parametrize(
    "role",
    ['casting_assistant', 'casting_director', 'executive_producer']
)
def test_404_when_get_movie_unexistent_id(client, token_header, role):
    response = client.get('/movies/8484958',
                          headers=token_header[role])
    verifies_404_response(response)


@pytest.mark.parametrize("role", ['executive_producer'])
def test_post_movies(client, token_header, role):
    total_movies_before_post = Movie.query.count()
    new_movie = {
        "title": "Godzilla vs. King Kong",
        "release_date": "2021-07-23"
    }

    response = client.post('/movies',
                           json=new_movie,
                           headers=token_header[role])
    assert response.status_code == 201

    total_movies_after_post = Movie.query.count()
    assert total_movies_before_post + 1 == total_movies_after_post

    data = response.get_json()
    assert data['success']

    movie_created = data['movie']
    assert movie_created['id'] is not None
    assert movie_created['title'] == new_movie['title']
    assert movie_created['release_date'] == new_movie['release_date']


@pytest.mark.parametrize("role", ['executive_producer'])
def test_422_in_post_movies_invalid_fields(client, token_header, role):
    malformed_movie = {
        "titlle": "Fantastic Four"
    }
    response = client.post('/movies',
                           json=malformed_movie,
                           headers=token_header[role])
    verifies_422_response(response)


@pytest.mark.parametrize("role", ['executive_producer'])
def test_400_in_post_movies_body_malformed(client, token_header, role):
    response = client.post('/movies',
                           json="Malformed",
                           headers=token_header[role])
    verifies_400_response(response)


@pytest.mark.parametrize("role", ['casting_assistant', 'casting_director'])
def test_401_post_movies_with_unauthorized_roles(client, token_header, role):
    new_movie = {
        "title": "Godzilla vs. King Kong",
        "release_date": "2021-07-23"
    }
    response = client.post('/movies',
                           json=new_movie,
                           headers=token_header[role])
    verifies_401_lack_of_permissions(response)


@pytest.mark.parametrize(
    "role, field_patched, new_value, movie_id",
    [('casting_director', 'release_date', "2021-03-19", 3),
     ('executive_producer', 'release_date', "2022-03-19", 4),
     ('casting_director', 'title', 'Fortitude of Solitude', 5),
     ('executive_producer', 'title', 'Captain Puerto Rico', 6)]
)
def test_patch_movie(client, token_header, role, field_patched, new_value, movie_id):
    patch_body = {
        field_patched: new_value
    }
    movie_before_patch = Movie.query.get(movie_id).format()
    response = client.patch(f'/movies/{movie_id}',
                            json=patch_body,
                            headers=token_header[role])
    assert response.status_code == 200

    data = response.get_json()
    assert data['success']

    movie_after_patch = data['movie']
    for field, value in movie_after_patch.items():
        if field == field_patched:
            assert value != movie_before_patch[field]
            assert value == patch_body[field]
        else:
            assert value == movie_after_patch[field]


@pytest.mark.parametrize("role", ['casting_director', 'executive_producer'])
def test_404_in_patch_movie_unexistent_id(client, token_header, role):
    response = client.patch('/movies/949489',
                            json={"title": "Titanic 2"},
                            headers=token_header[role])
    verifies_404_response(response)


@pytest.mark.parametrize("role", ['casting_director', 'executive_producer'])
def test_422_in_patch_movie_invalid_fields(client, token_header, role):
    response = client.patch('/movies/5',
                            json={"tittle": "Titanic 3"},
                            headers=token_header[role])
    verifies_422_response(response)


@pytest.mark.parametrize("role", ['casting_director', 'executive_producer'])
def test_400_in_patch_movie_malformed_request(client, token_header, role):
    response = client.patch('/movies/1',
                            json="Malformed request",
                            headers=token_header[role])
    verifies_400_response(response)


@pytest.mark.parametrize("role", ['casting_assistant'])
def test_401_in_patch_movie_unauthorized_role(client, token_header, role):
    response = client.patch('/movies/5',
                            json={'release_date': '2023-04-23'},
                            headers=token_header[role])
    verifies_401_lack_of_permissions(response)


@pytest.mark.parametrize(
    "role, movie_id",
    [("executive_producer", 20)]
)
def test_delete_movie(client, token_header, role, movie_id):
    response = client.delete(f'/movies/{movie_id}',
                             headers=token_header[role])
    assert response.status_code == 200

    data = response.get_json()
    assert data['success']


@pytest.mark.parametrize(
    "role, movie_id",
    [("executive_producer", 2000)]
)
def test_404_delete_movie_with_non_existent_id(client, token_header, role, movie_id):
    response = client.delete(f'/movies/{movie_id}',
                             headers=token_header[role])
    verifies_404_response(response)


@pytest.mark.parametrize(
    "role, movie_id",
    [("casting_assistant", 19),
     ("casting_director", 18)]
)
def test_401_delete_movie_with_unauthorized_roles(client, token_header, role, movie_id):
    response = client.delete(f'/movies/{movie_id}',
                             headers=token_header[role])
    verifies_401_lack_of_permissions(response)


@pytest.mark.parametrize(
    "role",
    ['casting_assistant', 'casting_director', 'executive_producer']
)
def test_get_actors_default_page(client, token_header, role):
    response = client.get('/actors',
                          headers=token_header[role])
    assert response.status_code == 200

    actors = [a.format() for a in Actor.query.order_by(Actor.id).slice(0, 10)]
    total_actors = Actor.query.count()

    data = response.get_json()

    assert data['success']
    assert data['actors'] == actors
    assert data['total_actors'] == total_actors


@pytest.mark.parametrize(
    "role",
    ['casting_assistant', 'casting_director', 'executive_producer']
)
def test_get_actors_second_page(client, token_header, role):
    response = client.get('/actors',
                          query_string={'page': 2},
                          headers=token_header[role])
    assert response.status_code == 200

    actors = [a.format() for a in Actor.query.order_by(Actor.id).slice(10, 20)]
    total_actors = Actor.query.count()

    data = response.get_json()

    assert data['success']
    assert data['actors'] == actors
    assert data['total_actors'] == total_actors


@pytest.mark.parametrize(
    "role",
    ['casting_assistant', 'casting_director', 'executive_producer']
)
def test_404_if_get_actors_unexistent_page(client, token_header, role):
    response = client.get('/actors',
                          query_string={'page': 2009},
                          headers=token_header[role])
    verifies_404_response(response)


@pytest.mark.parametrize(
    "role",
    ['casting_assistant', 'casting_director', 'executive_producer']
)
def test_get_actor(client, token_header, role):
    response = client.get('/actors/1',
                          headers=token_header[role])
    assert response.status_code == 200

    a = Actor.query.get(1)
    data = response.get_json()

    assert data['success']

    actor = data['actor']
    assert actor['id'] == a.id
    assert actor['name'] == a.name
    assert actor['age'] == a.age
    assert actor['gender'] == a.gender.value


@pytest.mark.parametrize(
    "role",
    ['casting_assistant', 'casting_director', 'executive_producer']
)
def test_404_when_get_actor_unexistent_id(client, token_header, role):
    response = client.get('/actors/9000',
                          headers=token_header[role])
    verifies_404_response(response)


@pytest.mark.parametrize("role", ['casting_director', 'executive_producer'])
def test_post_actors(client, token_header, role):
    total_actors_before_post = Actor.query.count()
    new_actor = {
        "name": "John Brubeck",
        "age": 36,
        "gender": "male"
    }

    response = client.post('/actors',
                           json=new_actor,
                           headers=token_header[role])
    assert response.status_code == 201

    total_actors_after_post = Actor.query.count()
    assert total_actors_before_post+1 == total_actors_after_post

    data = response.get_json()
    assert data['success']

    actor_created = data['actor']
    assert actor_created['id'] is not None
    assert actor_created['name'] == new_actor['name']
    assert actor_created['age'] == new_actor['age']
    assert actor_created['gender'] == new_actor['gender']


@pytest.mark.parametrize("role", ['casting_director', 'executive_producer'])
def test_422_in_post_actors_invalid_fields(client, token_header, role):
    malformed_actor = {
        "name": "Fantastic Four",
        "aaage": 74
    }
    response = client.post('/actors',
                           json=malformed_actor,
                           headers=token_header[role])
    verifies_422_response(response)


@pytest.mark.parametrize("role", ['casting_director', 'executive_producer'])
def test_400_in_post_actors_body_malformed(client, token_header, role):
    response = client.post('/actors',
                           json="request body malformed",
                           headers=token_header[role])
    verifies_400_response(response)


@pytest.mark.parametrize("role", ['casting_assistant'])
def test_401_post_actors_with_unauthorized_roles(client, token_header, role):
    new_actor = {
        "name": "Jane Brubeck",
        "age": 26,
        "gender": "female"
    }
    response = client.post('/actors',
                           json=new_actor,
                           headers=token_header[role])
    verifies_401_lack_of_permissions(response)


@pytest.mark.parametrize(
    "role, field_patched, new_value, actor_id",
    [("casting_director", "name", "Yukio Mishima", 3),
     ("executive_producer", "name", "Robbie Reiss", 4),
     ("casting_director", "age", 20, 5),
     ("executive_producer", "age", 67, 6),
     ("casting_director", "gender", "male", 7),
     ("executive_producer", "gender", "female", 8)]
)
def test_patch_actor(client, token_header, role, field_patched, new_value, actor_id):
    actor_before_patch = Actor.query.get(actor_id).format()
    patch_actor = {
        field_patched: new_value
    }

    response = client.patch(f'/actors/{actor_id}',
                            json=patch_actor,
                            headers=token_header[role])
    assert response.status_code == 200

    data = response.get_json()
    assert data['success']

    actor_after_patch = data['actor']
    for field, value in actor_after_patch.items():
        if field == field_patched:
            assert value != actor_before_patch[field]
            assert value == patch_actor[field]
        else:
            assert value == actor_before_patch[field]


@pytest.mark.parametrize("role", ['casting_director', 'executive_producer'])
def test_404_in_patch_actor_unexistent_id(client, token_header, role):
    response = client.patch('/actors/111021',
                            json={"name": "Romeo Bautista"},
                            headers=token_header[role])
    verifies_404_response(response)


@pytest.mark.parametrize("role", ['casting_director', 'executive_producer'])
def test_422_in_patch_actor_invalid_fields(client, token_header, role):
    response = client.patch('/actors/5',
                            json={"aaage": "Titanic 3"},
                            headers=token_header[role])
    verifies_422_response(response)


@pytest.mark.parametrize("role", ['casting_director', 'executive_producer'])
def test_400_in_patch_actor_malformed_request(client, token_header, role):
    response = client.patch('/actors/6',
                            json="Malformed request",
                            headers=token_header[role])
    verifies_400_response(response)


@pytest.mark.parametrize("role", ['casting_assistant'])
def test_401_in_patch_actor_unauthorized_role(client, token_header, role):
    response = client.patch('/actors/5',
                            json={'gender': 'male'},
                            headers=token_header[role])
    verifies_401_lack_of_permissions(response)


@pytest.mark.parametrize(
    "role, actor_id",
    [("casting_director", 19),
     ("executive_producer", 20)]
)
def test_delete_actor(client, token_header, role, actor_id):
    response = client.delete(f'/actors/{actor_id}',
                             headers=token_header[role])
    assert response.status_code == 200

    data = response.get_json()
    assert data['success']


@pytest.mark.parametrize(
    "role, actor_id",
    [("casting_director", 1900),
     ("executive_producer", 2020)]
)
def test_404_delete_actor_with_non_existent_id(client, token_header, role, actor_id):
    response = client.delete(f'/actors/{actor_id}',
                             headers=token_header[role])
    verifies_404_response(response)


@pytest.mark.parametrize(
    "role, actor_id",
    [("casting_assistant", 18)]
)
def test_401_delete_actor_with_unauthorized_roles(client, token_header, role, actor_id):
    response = client.delete(f'/actors/{actor_id}',
                             headers=token_header[role])
    verifies_401_lack_of_permissions(response)


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
