from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Movie, Actor
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
        response = Movie.query.get_or_404(movie_id).format()
        response['success'] = True
        return jsonify(response)

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

    @app.errorhandler(404)
    def not_found_handler(error):
        return jsonify(
            success=False,
            error=error.code,
            message="Resource not found"
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
