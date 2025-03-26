from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass


class MainForm(FlaskForm):
    rating = FloatField('Your rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Update')


class AddForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top_movie.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(1000), nullable=True)
    img_url: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f"<Movie{self.title}>"


with app.app_context():
    db.create_all()


@app.route("/")
def home():

    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_entries = result.scalars().all()

    for i in range(len(all_entries)):
        all_entries[i].ranking = len(all_entries) - i
    db.session.commit()

    return render_template("index.html", data=all_entries)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    edit_form = MainForm()
    if edit_form.validate_on_submit():
        rating = edit_form.rating.data
        review = edit_form.review.data

        movie_id = request.args.get('id')
        movie_to_update = db.get_or_404(Movie, movie_id)
        movie_to_update.rating = rating
        movie_to_update.review = review
        db.session.commit()
        return redirect(url_for('home'))
    return  render_template('edit.html', form=edit_form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')

    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    add_title = AddForm()
    if add_title.validate_on_submit():
        the_title = add_title.movie_title.data

        # making a request to movie db api
        url = f"https://api.themoviedb.org/3/search/movie?query={the_title}&include_adult=false&language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlYmM5YzgxNWRiMTZkZjZhMzU4ZWRiMjE0MjQzODg0NCIsIm5iZiI6MTc0MjkyNzU0NC4zMzMsInN1YiI6IjY3ZTJmNmI4ZWJhNzlmNmZmN2YwYTA4NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8Q1bf8B5D0AuuLVhA_3nPR2NQP1MmHoDCGiRb8DBasw"
        }
        response = requests.get(url, headers=headers)
        data = response.json()["results"]
        return render_template("select.html", results=data)

    return render_template("add.html", form=add_title)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
        url = f"https://api.themoviedb.org/3/movie/{movie_api_id}?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlYmM5YzgxNWRiMTZkZjZhMzU4ZWRiMjE0MjQzODg0NCIsIm5iZiI6MTc0MjkyNzU0NC4zMzMsInN1YiI6IjY3ZTJmNmI4ZWJhNzlmNmZmN2YwYTA4NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8Q1bf8B5D0AuuLVhA_3nPR2NQP1MmHoDCGiRb8DBasw"
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
