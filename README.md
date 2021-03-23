# Casting Agency API

The purpose of this API is helping assistants, directors & producers to manage
the talent and the projects they are currently working on. It provides endpoints
for handling information about actors that they are considering to cast, and
data about future projects.

The main motivation of implementing this application is demonstrate the skills
learned from Udacity Full Stack Nanodegree program, and it integrates some of
the technologies used there: representing models using SQLAlchemy, implementing
and API using Flask, provide authentication through Auth0.


## Installation
Before installation, install or update your Python runtime to version 3.8,
Then clone this repository and set up a virtual environment by using `venv`
module. If you haven't done this before, you can follow a guide
[right in this link](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

After setting up the virtual environment, you can install the project 
dependencies using pip:

```bash
pip install -r requirements.txt
```


## Running the API

### Enviroment variables
Before running the app, some environment variables should be set up. These 
variables are related with SQLAlchemy & Auth0 settings. Be sure to include them
in the environment where you run this app:

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
After setting up the corresponding variables, you can run the API locally using 
Flask. Set up Flask for running the `app` module in a development environment
and then run it:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

The app will be running in the URL http://localhost:5000.

An alternative way is to run the `app.py` script directly:

```bash
python3 app.py
```

In this other way, the app is set up to run in port 8080 with debug mode on.
You can change this by modifying the app.run sentence, located in the __main__
block at the end of the script:

```python
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
```

### Testing the API
A suite of [pytest](https://docs.pytest.org/en/stable/) unit tests is provided
in `test_app.py` module. Before running the tests, load the environment
variables from the `setup.sh` script.

There are two pytest fixtures that include testing configuration. The main one
is the `client` fixture:

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
In this fixture you can configure a URL to connect to a local testing database,
through the database variables before `test_config`.
[Consult the SQLAlchemy guide](https://docs.sqlalchemy.org/en/latest/core/engines.html?highlight=create_engine#database-urls)
for filling the corresponding values.

This fixture also includes a `load_data` function, imported from the 
`data_loader` module. It inserts some rows in the database before the tests.
Drop and create the testing database before running the tests. If you're using
PostgreSQL, this can be done in this way:

```bash
dropdb testing_database
createdb testing_database
```

The second fixture that includes testing configuration is `token_header`:

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

It provides a dictionary with authorization headers for the three different 
roles associated with this application (these roles are described in the next
section). If you want to include your own tokens, pass them to the
`get_authorization_header` functions.

**Note**: This tests take the same configuration included in the Auth0
environment variables, it is necessary to load them from `setup.sh`.

For running the test, just run pytest:
```bash
pytest
```

Or run the `test_app` module:
```bash
python test_app.py
```


## Access roles & permissions
The access to this API's endpoint is segmented in 3 different roles:
_casting assistant_, _casting director_ and _executive producer_.

* The casting assistant helps a casting director in the search of actors & 
  actresses for different projects.
* The casting director casts actors and checks to which movie assign them.
* The executive producer is the responsible of production of different movies.

The permissions assigned to these roles are the following:
* Casting assistant:
  * `get:movies`
  * `get:actors`
* Casting director:
  * All the permissions of a casting assistant
  * `post:actors`
  * `update:actors`
  * `delete:actors`
  * `update:movies`
* Executive producer:
  * All the permissions of a casting director
  * `post:movies`
  * `delete:movies`
  
The permissions map directly the endpoints of this API.

## API Endpoints

### GET /movies
It returns a paginated list of movies & the total number of movies saved.

* Request arguments:
  - `page`: indicate the page number requested (e. g. `/movies?page=3`)
* Response body fields:
  - `success`: boolean value that indicates if the request has been successful.
  - `movies`: contains a list of movies, at most 10 for every page.
  - `total_movies`: total number of movies included in the database.
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
  - `movie`: JSON object corresponding to the posted movie.
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
just update the fields passed in the request body.

* Request body fields:
  - `title`: Title of the movie.
  - `release_date`: Release date of the movie in [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html).
* Response body fields:
  - `success`: boolean value that indicates if the request has been successful.
  - `movie`: JSON object corresponding to the updated movie.
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
It returns a paginated list of actors & the total number of actors saved.

* Request arguments:
  - `page`: indicate the page number requested (e. g. `/actors?page=3`)
* Response body fields:
  - `success`: boolean value that indicates if the request has been succesful.
  - `actors`: contains a list of actors, at most 10 for every page.
  - `total_actors`: total number of actors included in the database.
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
  - `actor`: JSON object with the posted actor.
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
will just update the fields passed in the request body.

* Request body fields:
  - `name`: Name of the actor.
  - `age`: Age of the actor.
  - `gender`: Gender of the actor. As in the POST /actors endpoint, it just
  accepts two values: `male` or `female`.
* Response body fields:
  - `success`: boolean value that indicates if the request has been successful.
  - `actor`: JSON object with the updated actor.
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
  - `success`: boolean value that indicates the request has failed by holding a
    false value.
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

## Trying this API live
This app is hosted at Heroku, in the following URL:
https://diegoehg-casting-agency-api.herokuapp.com/

For testing it, a Postman collection is provided in this repository, with JWTs
for accessing the different endpoints. This JWTs are located in the variables 
section of the collection, at the end of the file:

```json
{
  "variable": [
    {
      "key": "casting-assistant-token",
      "value": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMGRmNmI2ZmZjYmUyMDA2YTg4NmUyZCIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2NDEyNDM4LCJleHAiOjE2MTY0OTg4MzgsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.CTqWa5XBwyMMaZ6UobUDujenF5ezLewoSyYVd4wM3QBIwStDPOS0QNr9udmFr0mkSQYZYXLCQmSuwd9p1_CZk0HiZaP96rQsTqSKmlBsdOGvS-ZvZ_BiJVGumdrL-GrlZWPZnOcoXyLuKX2haokmS23ZrYYNQBq6U1kz7-sLganj_0X9EDz9fyEDqaSOYlJ-pJt8-7pE8cpfgO41YTm9CwXNX0bwqGn1jdDF9GHQAg7rD9J7e_m2pAbIOABI_qY9ny65m1PmM4YXSwcla4nRWn9XT51jnzkfHdVwBXHNuBVMOm9FIW1RXPmy0LeDwk9Eq78t5fAPCduWdsUlCnalvA"
    },
    {
      "key": "casting-director-token",
      "value": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNTJiMmQ1ODQzNWRhMDA2ODg0ODI2OSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2NDEyNDk4LCJleHAiOjE2MTY0OTg4OTgsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.QUvFTLUNVEIIIRyuCL1HasGYeVVeBEDxeSjeEFHA4M0F-ygMMCazvDufka3xVEJgzSGsfvOGHs18cwGqj0cytPhN4b1_UBeOE2KkwBF_Gtdm76ySxKm5RN1Ql45KTzHZqx-QrvnZi_g7qbffpuIoUZUYECpJLYNHgZ3ZaJ-Zj65X3AEZV6gnmIGHuh3nMz2bku_YjUMzsLZJ1h4xzdrBobnLs7cYkah54PbYd-xdnlf8FfhF7wYGDJkRTz0JRVE8hggW-9-HH_n4-pBbNCa7O4DSq_MK78Q_j3ZBluqVXplnY_PwW8W-l_sUcasv2GMimhWyogQbSRBd1vS7enaFZg"
    },
    {
      "key": "executive-producer-token",
      "value": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllKTHRSdUJFM1QxVXVNR0VkTWdaeCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iYWxpYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNTJiNDY2MjYyNjFhMDA2ZmE5MGJhOSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5LWF1dGgtYXBpIiwiaWF0IjoxNjE2NDEyNjA0LCJleHAiOjE2MTY0OTkwMDQsImF6cCI6Ik9yQTZkRFZiVmVYZ01YQkFsVHFuWHI4UE9RU2MyYVY4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.eP_CF8BYHL1nfbVXnIc1_Rim4KwDTYO4wL5GfPmmLboNoXuIRYdcjJf7N7XpPVRTx-Uw6mizNtvqesRM8IwoEdix4YnSuoMmxyQ2kjdNo4EE53ZE9FE9YZJoRE3NIqVmcZc-CmI14M8iYlK0vhJGMsPsG0QXsU9Ec1Tr0iEbNetkpS7Vuqzb712JEznaEFqKlELyaaMh7r1Rf4XstC62hUo2m25CHkpAY4ZoJ0dlqcgyHc1DzF6Fe_QdtXpd0YAJvm17Mw9kBcV76RN5_JyWHEZSWNZaqWJwqddjUGsltFHk3ei-dyPe8a9sEcP6bdDUG4F70KWMBYISEjMd79DTyw"
    }
  ]
}
```

Load this collection from Postman and give it a try!

## License
All of the files included in this project are covered by the 
[MIT License](https://github.com/diegoehg/casting-agency-api/blob/main/LICENSE).
