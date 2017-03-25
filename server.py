from flask import Flask, render_template
from jinja2 import StrictUndefined
import os, requests, json
from pprint import pprint

# MovieDB API key
tmdb_api_key = os.environ['TMDB_API_KEY']
owm_api_key = os.environ['OWM_API_KEY']

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


@app.route('/search_movies')
def search_movies():
    """Takes search movies and display results list."""
    search_term = 'Indiana+Jones'

    tmdb_url = 'https://api.themoviedb.org/3/search/movie?api_key=%s&query=%s' % (tmdb_api_key, search_term)

    tmdb_request = requests.get(tmdb_url)
    response = tmdb_request.json()
    movies = response['results']

    return render_template('search_results.html',movies=movies)


@app.route('/local_weather')
def get_local_weather():
    """Display local weather from OpenWeatherMap."""

    owm_url = 'http://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=%s' % (owm_api_key)

    owm_request = requests.get(owm_url)
    # pprint(r.json())
    weather_info = owm_request.json()
    pprint(weather_info)
    # print weather_info['name']

    return render_template('local_weather.html',weather_info=weather_info)

if __name__ == "__main__":
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.run(host="0.0.0.0")
