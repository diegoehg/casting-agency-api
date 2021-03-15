import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie


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
    def get_movies():
        page_number = request.args.get('page', 1, type=int)
        movies = get_paginated_movies(page_number)

        return jsonify(success=True,
                       movies=movies,
                       total_movies=Movie.query.count())

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
