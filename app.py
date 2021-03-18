from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Movie
from auth import requires_auth, AuthException

MOVIES_PER_PAGE = 10


def get_paginated_movies(page_number):
    start_index = (page_number - 1) * MOVIES_PER_PAGE
    end_index = start_index + MOVIES_PER_PAGE
    questions_page = Movie.query.order_by(Movie.id).slice(start_index, end_index)
    return [q.format() for q in questions_page]


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
    def get_movies(payload):
        page_number = request.args.get('page', 1, type=int)
        movies = get_paginated_movies(page_number)

        if len(movies) == 0:
            abort(404)

        return jsonify(
            success=True,
            movies=movies,
            total_movies=Movie.query.count()
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
