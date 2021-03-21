from datetime import date
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, db, Movie, Actor, Gender
from auth import requires_auth, AuthException


def get_paginated_query(query, ordering_column, page_number=1, rows_by_page=10):
    start_index = (page_number - 1) * rows_by_page
    end_index = start_index + rows_by_page
    rows = query.order_by(ordering_column).slice(start_index, end_index)
    return [r.format() for r in rows]


def create_app(test_config=None):
    """
    Create and configure the app
    """
    app = Flask(__name__)
    if test_config is None:
        setup_db(app)
    else:
        setup_db(app, test_config['DATABASE_URL'])

    CORS(app)

    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies():
        page_number = request.args.get('page', 1, type=int)
        movies = get_paginated_query(Movie.query, Movie.id, page_number)

        if len(movies) == 0:
            abort(404)

        return jsonify(
            success=True,
            movies=movies,
            total_movies=Movie.query.count()
        )

    @app.route('/movies/<int:movie_id>')
    @requires_auth('get:movies')
    def get_movie(movie_id):
        m = Movie.query.get_or_404(movie_id)

        return jsonify(
            success=True,
            movie=m.format()
        )

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movies():
        try:
            new_movie = request.get_json()
            m = Movie(
                new_movie['title'],
                date.fromisoformat(new_movie['release_date'])
            )
            m.insert()

            return jsonify(
                success=True,
                movie=m.format()
            ), 201

        except TypeError:
            db.session.rollback()
            abort(400)

        except KeyError:
            db.session.rollback()
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('update:movies')
    def patch_movie(movie_id):
        m = Movie.query.get_or_404(movie_id)
        patch_data = request.get_json()

        if not isinstance(patch_data, dict):
            abort(400)

        if 'title' not in patch_data and 'release_date' not in patch_data:
            abort(422)

        if 'title' in patch_data:
            m.title = patch_data['title']

        if 'release_date' in patch_data:
            m.release_date = date.fromisoformat(patch_data['release_date'])

        m.update()

        return jsonify(
            success=True,
            movie=m.format()
        )

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(movie_id):
        m = Movie.query.get_or_404(movie_id)
        m.delete()
        return jsonify(success=True)

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors():
        page_number = request.args.get('page', 1, type=int)
        actors = get_paginated_query(Actor.query, Actor.id, page_number)

        if len(actors) == 0:
            abort(404)

        return jsonify(
            success=True,
            actors=actors,
            total_actors=Actor.query.count()
        )

    @app.route('/actors/<int:actor_id>')
    @requires_auth('get:actors')
    def get_actor(actor_id):
        a = Actor.query.get_or_404(actor_id)

        return jsonify(
            success=True,
            actor=a.format()
        )

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actors():
        try:
            new_actor = request.get_json()
            a = Actor(
                new_actor['name'],
                new_actor['age'],
                Gender(new_actor['gender'])
            )
            a.insert()

            return jsonify(
                success=True,
                actor=a.format()
            ), 201

        except TypeError:
            db.session.rollback()
            abort(400)

        except KeyError:
            db.session.rollback()
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('update:actors')
    def patch_actor(actor_id):
        a = Actor.query.get_or_404(actor_id)
        patch_data = request.get_json()

        if not isinstance(patch_data, dict):
            abort(400)

        if 'name' not in patch_data and 'age' not in patch_data \
                and 'gender' not in patch_data:
            abort(422)

        if 'name' in patch_data:
            a.name = patch_data['name']

        if 'age' in patch_data:
            a.age = patch_data['age']

        if 'gender' in patch_data:
            a.gender = Gender(patch_data['gender'])

        a.update()

        return jsonify(
            success=True,
            actor=a.format()
        )

    @app.errorhandler(400)
    def malformed_request_handler(error):
        return jsonify(
            success=False,
            error=error.code,
            message='The server cannot process the request'
        ), error.code

    @app.errorhandler(404)
    def not_found_handler(error):
        return jsonify(
            success=False,
            error=error.code,
            message="Resource not found"
        ), error.code

    @app.errorhandler(405)
    def method_not_allowed_handler(error):
        return jsonify(
            success=False,
            error=error.code,
            message="Method not allowed"
        ), error.code

    @app.errorhandler(422)
    def unprocessable_entity_handler(error):
        return jsonify(
            success=False,
            error=error.code,
            message="The request was well-formed but was unable to be followed due to semantic errors"
        ), error.code

    @app.errorhandler(AuthException)
    def authorization_exception_handler(exception):
        return jsonify(
            success=False,
            error=exception.status_code,
            message=exception.message
        ), exception.status_code

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
