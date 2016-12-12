from flask import Flask, render_template
from jinja2 import StrictUndefined
import os, requests, json

# MovieDB API key
tmdb_api_key = os.environ['TMDB_API_KEY']
tmdb_url = 'https://api.themoviedb.org/3/movie/550?api_key=%s' % (tmdb_api_key)

app = Flask(__name__)

@app.route('/')
def index():
    """Display list of APIs"""

    return render_template('index.html')

@app.route('/movie/<int:tmdb_id>')
def display_tmdb_movie(tmdb_id):
    """Display movie details from the Movie DB."""

    tmdb_url = 'https://api.themoviedb.org/3/movie/%s?api_key=%s' % (tmdb_id, tmdb_api_key)

    tmdb_request = requests.get(tmdb_url)
    movie = tmdb_request.json()

    return render_template('movie.html', movie=movie)


if __name__ == "__main__":
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.run(host="0.0.0.0")
