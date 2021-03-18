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


## License
All of the files included in this project are covered by the 
[MIT License](https://github.com/diegoehg/casting-agency-api/blob/main/LICENSE).
