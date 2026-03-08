from flask import render_template, request, Blueprint
from app.services import TMDBService
import os

bp = Blueprint('main', __name__)
tmdb_service = TMDBService(os.environ.get('TMDB_API_KEY'))

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        movie_title = request.form.get('movie_title')
        movies = tmdb_service.search_movie(movie_title)
        return render_template('index.html', movies=movies)
    return render_template('index.html')

@bp.route('/recommendations/<int:movie_id>')
def recommendations(movie_id):
    recommendations = tmdb_service.get_movie_recommendations(movie_id)
    return render_template('recommendations.html', recommendations=recommendations)
