import os

TMDB_TOKEN_BEARER = os.getenv('TMDB_TOKEN_BEARER')
FLASK_CONFIG_SECRET_KEY = os.getenv('FLASK_CONFIG_SECRET_KEY')

MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie/"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/original"
