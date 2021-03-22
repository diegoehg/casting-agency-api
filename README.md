# Casting Agency API

The purpose of this API is helping assistants, directors & producers to manage
the talent and the projects they are currently working on. This API provides
endpoints for handling information about actors and movies.


## Installation
For installing this application locally, clone this repository and install 
the requirements listed:

```bash
pip install -r requirements.txt
```
It is recommended to do it in a virtual environment, 
[by using `venv` module](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).


## Running the API

### Enviroment variables
Before running the app, some environment variables should be set up for
its correct execution. These variables are related with SQLAlchemy & Auth0
settings. Be sure to include them in the environment where you run this app:

* `DATABASE_URL`: contains the configuration for connecting to the database.
[Follow the SQLAlchemy guide for composing this URL](https://docs.sqlalchemy.org/en/latest/core/engines.html?highlight=create_engine#database-urls).
* `AUTH0_DOMAIN`: contains the URL of Auth0 domain which is used to validate
authorization tokens.
* `ALGORITHMS`: contains an array with algorithms used for encrypting the JWT.
* `API_AUDIENCE`: contains the identifier of the Auth0 API which is associated
with this API.

These variables are listed in the `setup.sh` script, so you can load them
right from there:

```bash
source setup.sh
```

### Running Flask
After setting up the corresponding variables, you can run the API locally
by running the `app` module:

```bash
python3 app.py
```

In this module, the app is set up to run in port 8080 and with debug mode on,
you can change this by modifying the app.run sentence on the __main__ block:

```python
if __name__ == '__main__':
  APP.run(host='0.0.0.0', port=8080, debug=True)
```

### Testing the API
A suite of unit tests is provided in `test_app.py` module, implemented using
pytest. It was chosen pytest over unittest because it's more easier to
parametrize the tests, and in some cases the same endpoint test is run against
two or three different role JWTs.

There are two pytest fixture where you can configure the tests. The main one is
the client fixture:

```python
@pytest.fixture(scope='module')
def client():
  database_dialect = "postgresql"
  database_user = "tester_user"
  database_password = "password_testing_user"
  database_location = "localhost:5432"
  database_name = "testing_database"

  test_config = {
    'DATABASE_URL': f"{database_dialect}://{database_user}:{database_password}@{database_location}/{database_name}"
  }

  app = create_app(test_config)
  with app.test_client() as testing_client:
    with app.app_context():
      db.create_all()
      load_data()
      yield testing_client
```
In this fixture you can configure a URL to connect to a testing database,
[by following the SQLAlchemy guide](https://docs.sqlalchemy.org/en/latest/core/engines.html?highlight=create_engine#database-urls).
There is included a `load_data` function imported from the `data_loader`
module. This functions inserts some Movie and Actor rows for running the tests.
Drop and create the database before running the tests. If you're using 
PostgreSQL, this can be done by running:

```bash
dropdb testing_database
createdb testing_database
```

The second fixture where you can configure the tests is `token_header`:

```python
@pytest.fixture(scope='module')
def token_header():
  def get_authorization_header(token):
    return {
      'Authorization': f'Bearer {token}'
    }

  return {
    "casting_assistant": get_authorization_header("casting_assistant_JWT"),
    "casting_director": get_authorization_header("casting_director_JWT"),
    "executive_producer": get_authorization_header("executive_producer_JWT")
  }
```

In this fixture, is provided a dictionary with authorization headers for the
three different roles associated with this application (these roles are 
described in the next section). Before running the tests, introduce the 
corresponding JWTs to the `get_authorization_header` function.

After configuring the database and the JWTs, you can run the tests in these
two ways:

```bash
pytest

python3 test_app.py
```

## Access roles & permissions
This API is segmented for being used by 3 different roles: _casting assistant_,
_casting director_ and _executive producer_.

* The casting assistant assists a casting director in the search of actors & 
  actresses for different projects.
* The casting director cast actors and checks to which movie assign them.
* The executive producer is the responsible of production of different movies.

The permissions assigned to these roles are the following:
* Casting assistant:
  * `get:movies`
  * `get:actors`
* Casting director:
  * All the permissions of a casting asistant
  * `post:actors`
  * `update:actors`
  * `delete:actors`
  * `update:movies`
* Executive producer:
  * All the permissions of a casting director
  * `post:movies`
  * `delete:movies`

## API Endpoints

### GET /movies
It returns a paginated list of movies & the total number of movies saved in the
database.

* Request arguments:
  - `page`: indicate the page number requested (e. g. `/movies=?page=3`)
* Response body fields:
  - `success`: boolean value that indicates if the request has been succesful.
  - `movies`: contains a list of movies, at most 10 for every page.
  - `total_movies`: number of movies included in the database.
* Permission required: `get:movies`
  
Response body example:
```json
{
  "success": true,
  "movies": [
    {
      "id": 51,
      "title": "Avengers",
      "release_date": "2012-03-20"
    },
    {
      "id": 52,
      "title": "E. T.",
      "release_date": "1982-07-20"
    }
  ],
  "total_movies": 412
}
```

### GET /movies/{movie_id}
It returns the movie with the specified ID.

* Response body fields:
  - `success`: boolean value that indicates the request has been successful.
  - `movie`: JSON object with the following fields:
    - `id`: ID of the movie.
    - `title`: Title of the movie.
    - `release_date`: Release date of the movie.
* Permission required: `get:movies`
  
Response body example:
```json
{
  "success": true,
  "movie": {
    "id": 51,
    "title": "Avengers",
    "release_date": "2012-03-20"
  }
}
```

### POST /movies
It adds a new movie to the database.

* Request body fields:
  - `title`: Title of the movie.
  - `release_date`: Release date of the movie in [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html).
* Response body fields:
  - `success`: boolean value that indicates if the request has been successful.
  - `movie`: JSON object with same fields of request body plus a generated ID.
* Permission required: `post:movies`
  
Request body example:
```json
{
  "title": "Godzilla vs. King Kong",
  "release_date": "2021-03-28"
}
```

Response body example:
```json
{
  "success": true,
  "movie": {
    "id": 436,
    "title": "Godzilla vs. King Kong",
    "release_date": "2021-03-28"
  }
}
```

### PATCH /movies/{movie_id}
It updates the indicated fields of an existent movie.

The request body can have one of the movie fields, or both. This endpoint will
update just the fields passed.

* Request body fields:
  - `title`: Title of the movie.
  - `release_date`: Release date of the movie in [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html).
* Response body fields:
  - `success`: boolean value that indicates if the request has been successful.
  - `movie`: JSON object with requested movie data, including the updated field.
* Permission required: `update:movies`

Request body example:
```json
{
  "title": "Suspirium"
}
```

Response body example:
```json
{
  "success": true,
  "movie": {
    "id": 436,
    "title": "Suspirium",
    "release_date": "2021-03-28"
  }
}
```

### DELETE /movies/{movie_id}
It deletes the movie with the specified ID.

* Response body fields:
  - `success`: boolean value that indicates the request has been successful.
* Permission required: `delete:movies`

Response body example:
```json
{
  "success": true
}
```

### GET /actors
It returns a paginated list of actors & the total number of actors saved in the
database.

* Request arguments:
  - `page`: indicate the page number requested (e. g. `/actors=?page=3`)
* Response body fields:
  - `success`: boolean value that indicates if the request has been succesful.
  - `actors`: contains a list of actors, at most 10 for every page.
  - `total_actors`: number of actors included in the database.
* Permission required: `get:actors`

Response body example:
```json
{
  "success": true,
  "actors": [
    {
      "id": 34,
      "name": "Julia Robertson",
      "age": 47,
      "gender": "female"
    },
    {
      "id": 35,
      "name": "Chris Reeves",
      "age": 56,
      "gender": "male"
    }
  ],
  "total_actors": 412
}
```

### GET /actors/{actor_id}
It returns the actor with the specified ID.

* Response body fields:
  - `success`: boolean value that indicates the request has been successful.
  - `actor`: JSON object with the following fields:
    - `id`: ID of the actor.
    - `name`: Name of the actor.
    - `age`: Age of the actor.
    - `gender`: Gender of the actor.
* Permission required: `get:actors`

Response body example:
```json
{
  "success": true,
  "actor": {
    "id": 320,
    "name": "Robb Auerbach",
    "age": 32,
    "gender": "male"
  }
}
```

### POST /actors
It adds a new actor to the database.

* Request body fields:
  - `name`: Name of the actor.
  - `age`: Age of the actor.
  - `gender`: A string indicating the gender of the actor. Just two strings
    are allowed: `male` or `female`.
* Response body fields:
  - `success`: boolean value that indicates if the request has been successful.
  - `actor`: JSON object with same fields of request body plus a generated ID.
* Permission required: `post:actors`

Request body example:
```json
{
  "name": "Armin Arlett",
  "age": 18,
  "gender": "male"
}
```

Response body example:
```json
{
  "success": true,
  "actor": {
    "id": 302,
    "name": "Armin Arlett",
    "age": 18,
    "gender": "male"
  }
}
```

### PATCH /actors/{actor_id}
It updates the indicated fields of an existent actor.

The request body can have one of the actor fields, or all of them. This endpoint
will update just the fields passed.

* Request body fields:
  - `name`: Name of the actor.
  - `age`: Age of the actor.
  - `gender`: Gender of the actor. As in the POST /actors endpoint, it just
  accepts two values: `male` or `female`.
* Response body fields:
  - `success`: boolean value that indicates if the request has been successful.
  - `actor`: JSON object with requested actor data, including the updated fields.
* Permission required: `update:actors`

Request body example:
```json
{
  "name": "John Wock",
  "age": 58
}
```

Response body example:
```json
{
  "success": true,
  "actor": {
    "id": 436,
    "name": "John Wock",
    "age": 58,
    "gender": "male"
  }
}
```

### DELETE /actors/{actor_id}
It deletes the actor with the specified ID.

* Response body fields:
  - `success`: boolean value that indicates the request has been successful.
* Permission required: `delete:actors`

Response body example:
```json
{
  "success": true
}
```

### Errors response
In the case of errors, a JSON response is returned.

* Response body fields:
  - `success`: boolean value that indicates the request has successful. In the
    case of errors, it has a false value.
  - `error`: HTTP status code (e. g. 404, 401, 500).
  - `message`: A short description of the error.

Response body example:
```json
{
  "success": false,
  "error": 404,
  "message": "Resource not found"
}
```

## License
All of the files included in this project are covered by the 
[MIT License](https://github.com/diegoehg/casting-agency-api/blob/main/LICENSE).
