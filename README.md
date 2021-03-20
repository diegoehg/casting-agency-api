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
Before running the app, some environment variables should be set for
its correct execution. These variables are related with SQLAlchemy & Auth0
settings. Be aware to include them in the environment where you run this app:

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
For running the API, just execute the `app` module:

```bash
python3 app.py
```

### Testing the API
A suite of unit tests is provided in `test_app.py` module. You can compose an
URL to connect to a testing database. For running the suit of test, just run:

```bash
pytest
```

## Access roles
This API is segmented for being used by 3 different roles: _casting assistant_,
_casting director_ and _executive producer_.

* The casting assistant assists a casting director in the search of actors & 
  actresses for different projects.
* The casting director cast actors and assigns them to movies being produced.
* The executive producer is the responsible of production of different movies.

The permissions assign to these roles are the following:
* Casting assistant:
  * `get:movies`
  * `get:actors`
* Casting director:
  * All the permissions of casting asistant
  * `post:actors`
  * `update:actors`
  * `delete:actors`
  * `update:movies`
* Executive producer:
  * All the permissions of casting director
  * `post:movies`
  * `delete:movies`

## Endpoints

### GET /movies
It returns a paginated list of movies & the total number of movies kept in the
database.

* Request arguments:
  - `page`: indicate the page number requested (e. g. `/movies=?page=3`)
* Response fields:
  - `success`: boolean value that indicates if the request has been succesful.
  - `movies`: contains a list of movies, at most 10 for every page.
  - `total_movies`: number of movies included in the database.
* Permission required: `get:movies`
  
Response example:
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

* Request arguments: None
* Response fields:
  - `success`: boolean value that indicates the request has been successful.
  - `title`: Title of the movie.
  - `release_date`: Release date of the movie.
  
Response example:
```json
{
  "success": true,
  "id": 51,
  "title": "Avengers",
  "release_date": "2012-03-20"
}
```

### GET /actors
It returns a paginated list of actors & the total number of actors saved in the
database.

* Request arguments:
  - `page`: indicate the page number requested (e. g. `/actors=?page=3`)
* Response fields:
  - `success`: boolean value that indicates if the request has been succesful.
  - `actors`: contains a list of actors, at most 10 for every page.
  - `total_actors`: number of actors included in the database.
* Permission required: `get:actors`

Response example:
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

* Request arguments: None
* Response fields:
  - `success`: boolean value that indicates the request has been successful.
  - `id`: ID requested.
  - `name`: Name of the actor.
  - `age`: Age of the actor.
  - `gender`: Gender of the actor.

Response example:
```json
{
  "success": true,
  "id": 320,
  "name": "Robb Auerbach",
  "age": 32,
  "gender": "male"
}
```

### Errors response
In the case of errors, a JSON response is returned.

* Response fields:
  - `success`: boolean value that indicates the request has successful. In the
    case of errors, it has a false value.
  - `error`: HTTP status code (e. g. 404, 401, 500).
  - `message`: A short description of the error.

Response example:
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
