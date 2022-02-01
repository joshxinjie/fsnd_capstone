
import sys
import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def setup_db(app, database_uri):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    migrate = Migrate(app, db)

class Movie(db.Model):
    __tablename__ = 'Movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        # release_date_str = self.release_date.strftime("%d/%m/%Y")
        return '<Movie ID: {} | Title: {} | Release Date: {}>'.format(self.id, self.title, self.release_date)
    
    def format(self):
        return {
            'id': self.id,
            'title' : self.title,
            'release_date': self.release_date
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class Actor(db.Model):
    __tablename__ = 'Actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Actor ID: {} | Name: {} | Age: {} | Gender: {}>'.format(self.id, self.name, str(self.age), self.gender)

    def format(self):
        return {
            'id': self.id,
            'name' : self.name,
            'age': self.age,
            'gender': self.gender
        }
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

def db_init_sample_records():

    error = False
    
    try:
        movie_1 = Movie(
            title="Titanic",
            release_date = datetime.datetime(1997, 12, 19)
        )

        movie_2 = Movie(
            title="Avatar",
            release_date = datetime.datetime(2009, 12, 18)
        )

        actor_1 = Actor(
            name="Leonardo DiCaprio",
            gender="Male",
            age=25
        )

        actor_2 = Actor(
            name="Kate Winslet",
            gender="Female",
            age=25
        )

        movie_1_in_db_check = Movie.query.filter(Movie.title == movie_1.title).one_or_none()
        movie_2_in_db_check = Movie.query.filter(Movie.title == movie_2.title).one_or_none()
        actor_1_in_db_check = Actor.query.filter(Actor.name == actor_1.title).one_or_none()
        actor_2_in_db_check = Actor.query.filter(Actor.title == actor_2.title).one_or_none()

        if movie_1_in_db_check is None:
            movie_1.insert()
        if movie_2_in_db_check is None:
            movie_2.insert()
        if actor_1_in_db_check is None:
            actor_1.insert()
        if actor_2_in_db_check is None:
            actor_2.insert()
    except:
        error = True
        db.session.rollback()
        print("An error occured. Sample data cannot be inserted")
        print(sys.exc_info())