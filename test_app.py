import os
import json
import unittest
import datetime

from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor
from config import DEPLOYMENT, LOCAL_SQLALCHEMY_DATABASE_URI, HEROKU_SQLALCHEMY_DATABASE_URI

class CastingAgencyTestCase(unittest.TestCase):
    """
    This class represents the casting agency test case
    """

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client

        if DEPLOYMENT=="local":
            database_uri = LOCAL_SQLALCHEMY_DATABASE_URI
        elif DEPLOYMENT=="heroku":
            database_uri = HEROKU_SQLALCHEMY_DATABASE_URI
        setup_db(self.app, database_uri)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def test_retrieve_actors(self):
        res = self.client().get("/actors")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["actors"])

    def test_retrieve_movies(self):
        res = self.client().get("/movies")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["movies"])

    def test_delete_actor(self):
        # insert a test actor
        test_actor = Actor(
            name="Dummy",
            gender="Male",
            age=25
        )

        test_actor.insert()

        test_actor_id = Actor.query.filter(Actor.name == test_actor.name).one_or_none().id

        # delete question
        res = self.client().delete(
            "/actors/{}".format(test_actor_id)
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_delete_movie(self):
        # insert a test movie
        test_movie = Movie(
            title="Dummy",
            release_date = datetime.datetime(2000, 1, 1)
        )

        test_movie.insert()

        test_movie_id = Movie.query.filter(Movie.title == test_movie.title).one_or_none().id

        # delete question
        res = self.client().delete(
            "/movies/{}".format(test_movie_id)
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_post_actor(self):
        test_actor_body = {
            "name": "Dummy",
            "age": 30,
            "gender": "Male"
        }
        res = self.client().post("/actors", json=test_actor_body)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

        test_actor_id = data["actor"]["id"]
        self.assertTrue(test_actor_id)
        test_actor = Actor.query.filter(Actor.id == test_actor_id).one_or_none()
        test_actor.delete()

    def test_post_movie(self):
        test_movie_body = {
            "title": "Dummy",
            "release_date": "2022-01-15"
        }
        res = self.client().post("/movies", json=test_movie_body)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

        test_movie_id = data["movie"]["id"]
        self.assertTrue(test_movie_id)
        test_movie = Movie.query.filter(Movie.id == test_movie_id).one_or_none()
        test_movie.delete()

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()