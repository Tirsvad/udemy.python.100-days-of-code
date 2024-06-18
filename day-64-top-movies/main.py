from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, update, delete, values
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os.path
from constants import *

from rateMovieForm import RateMovieForm
from findMovieForm import FindMovieForm


app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_CONFIG_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top-movies.db"
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Create the extension
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(String(250), nullable=False)
    description: Mapped[float] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(String(250), nullable=True)
    ranking: Mapped[int] = mapped_column(String(250), nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


first_time_run = not os.path.isfile('./instance/top-movies.db')

with app.app_context():
    db.create_all()

if first_time_run:
    # Test data for db
    new_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's"
                    " sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads"
                    " to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    )

    second_movie = Movie(
        title="Avatar The Way of Water",
        year=2022,
        description="Set more than a decade after the events of the first film, learn the story of the Sully family "
                    "(Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each "
                    "other safe, the battles they fight to stay alive, and the tragedies they endure.",
        rating=7.3,
        ranking=9,
        review="I liked the water.",
        img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    )

    with app.app_context():
        db.session.add(new_movie)
        db.session.add(second_movie)
        db.session.commit()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))


    # Use .scalars() to get the elements rather than entire rows from the database
    all_movies = result.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", all_movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        headers = {"Authorization": f"Bearer {TMDB_TOKEN_BEARER}"}
        params = {"query": movie_title}
        response = requests.get(url=MOVIE_DB_SEARCH_URL, headers=headers, params=params)
        response.raise_for_status()
        result = response.json()["results"]
        return render_template("select.html", options=result)
    return render_template("add.html", form=form)

@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    # TODO delete movie
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        headers = {"Authorization": f"Bearer {TMDB_TOKEN_BEARER}"}
        movie_api_url = f"{MOVIE_DB_INFO_URL}{movie_api_id}"
        params = {'language': 'en-US'}
        response = requests.get(url=movie_api_url, headers=headers, params=params)
        response.raise_for_status()
        result = response.json()
        new_movie = Movie(
            title=result["title"],
            # The data in release_date includes month and day, we will want to get rid of.
            year=result["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{result['poster_path']}",
            description=result["overview"],
            rating=0,
            ranking=0,
            review=""
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
