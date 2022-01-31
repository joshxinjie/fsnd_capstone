import os
import json
import unittest
import datetime

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor
from config import DEPLOYMENT, LOCAL_SQLALCHEMY_DATABASE_URI, HEROKU_SQLALCHEMY_DATABASE_URI

load_dotenv()

CASTING_ASSISTANT_TOKEN = os.getenv('CASTING_ASSISTANT_TOKEN')
CASTING_DIRECTOR_TOKEN = os.getenv('CASTING_DIRECTOR_TOKEN')
EXECUTIVE_PRODUCER_TOKEN = os.getenv('EXECUTIVE_PRODUCER_TOKEN')

CASTING_ASSISTANT_AUTH_HEADER = {
    'Authorization': CASTING_ASSISTANT_TOKEN
}

CASTING_DIRECTOR_AUTH_HEADER = {
    'Authorization': CASTING_DIRECTOR_TOKEN
}

EXECUTIVE_PRODUCER_AUTH_HEADER = {
    'Authorization': EXECUTIVE_PRODUCER_TOKEN
}

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
    

    ##### CASTING ASSISTANT TESTS #####
    
    def test_retrieve_actors_casting_assistant(self):
        res = self.client().get("/actors", headers = CASTING_ASSISTANT_AUTH_HEADER)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["actors"])

    def test_retrieve_movies_casting_assistant(self):
        res = self.client().get("/movies", headers = CASTING_ASSISTANT_AUTH_HEADER)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["movies"])

    def test_delete_actor_casting_assistant(self):
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
            "/actors/{}".format(test_actor_id),
            headers = CASTING_ASSISTANT_AUTH_HEADER
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"], False)

        test_actor.delete()

    def test_patch_actor_casting_assistant(self):
        # insert a test actor
        test_actor = Actor(
            name="Dummy",
            gender="Male",
            age=25
        )

        test_actor.insert()

        test_actor_id = Actor.query.filter(Actor.name == test_actor.name).one_or_none().id

        updated_actor_body = {
            "name": "New Dummy",
            "age": 40
        }

        test_uri = "/actors/{}".format(test_actor_id)

        res = self.client().patch(test_uri, json=updated_actor_body, headers = CASTING_ASSISTANT_AUTH_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"], False)

        test_actor.delete()

    def test_patch_movie_casting_assistant(self):
        # insert a test movie
        test_movie = Movie(
            title="Dummy",
            release_date=datetime.datetime(2000, 1, 1)
        )

        test_movie.insert()

        test_movie_id = Movie.query.filter(Movie.title == test_movie.title).one_or_none().id

        updated_movie_body = {
            "title": "New Dummy",
            "release_date": "2022-01-15"
        }

        test_uri = "/movies/{}".format(test_movie_id)

        res = self.client().patch(test_uri, json=updated_movie_body, headers = CASTING_ASSISTANT_AUTH_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"], False)
        
    def test_post_actor_casting_assistant(self):
        test_actor_body = {
            "name": "Dummy",
            "age": 30,
            "gender": "Male"
        }
        res = self.client().post("/actors", json=test_actor_body, headers = CASTING_ASSISTANT_AUTH_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"], False)
    
    def test_post_movie_casting_assistant(self):
        test_movie_body = {
            "title": "Dummy",
            "release_date": "2022-01-15"
        }
        res = self.client().post("/movies", json=test_movie_body, headers = CASTING_ASSISTANT_AUTH_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"], False)

    def test_delete_movie_casting_assistant(self):
        # insert a test movie
        test_movie = Movie(
            title="Dummy",
            release_date = datetime.datetime(2000, 1, 1)
        )

        test_movie.insert()

        test_movie_id = Movie.query.filter(Movie.title == test_movie.title).one_or_none().id

        # delete question
        res = self.client().delete(
            "/movies/{}".format(test_movie_id),
            headers = CASTING_ASSISTANT_AUTH_HEADER
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"], False)

        test_movie.delete()


    ##### CASTING DIRECTOR TESTS #####

    def test_retrieve_actors_casting_director(self):
        res = self.client().get("/actors", headers = CASTING_DIRECTOR_AUTH_HEADER)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["actors"])

    def test_retrieve_movies_casting_director(self):
        res = self.client().get("/movies", headers = CASTING_DIRECTOR_AUTH_HEADER)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["movies"])

    def test_delete_actor_casting_director(self):
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
            "/actors/{}".format(test_actor_id),
            headers = CASTING_DIRECTOR_AUTH_HEADER
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_patch_actor_casting_director(self):
        # insert a test actor
        test_actor = Actor(
            name="Dummy",
            gender="Male",
            age=25
        )

        test_actor.insert()

        test_actor_id = Actor.query.filter(Actor.name == test_actor.name).one_or_none().id

        updated_actor_body = {
            "name": "New Dummy",
            "age": 40
        }

        test_uri = "/actors/{}".format(test_actor_id)

        res = self.client().patch(test_uri, json=updated_actor_body, headers = CASTING_DIRECTOR_AUTH_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["actor"]["name"], "New Dummy")
        self.assertEqual(data["actor"]["age"], 40)

        test_actor.delete()

    def test_patch_movie_casting_director(self):
        # insert a test movie
        test_movie = Movie(
            title="Dummy",
            release_date=datetime.datetime(2000, 1, 1)
        )

        test_movie.insert()

        test_movie_id = Movie.query.filter(Movie.title == test_movie.title).one_or_none().id

        updated_movie_body = {
            "title": "New Dummy",
            "release_date": "2022-01-15"
        }

        test_uri = "/movies/{}".format(test_movie_id)

        res = self.client().patch(test_uri, json=updated_movie_body, headers = CASTING_DIRECTOR_AUTH_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["movie"]["title"], "New Dummy")
        self.assertEqual(data["movie"]["release_date"], "Sat, 15 Jan 2022 00:00:00 GMT")

    def test_post_actor_casting_director(self):
        test_actor_body = {
            "name": "Dummy",
            "age": 30,
            "gender": "Male"
        }
        res = self.client().post("/actors", json=test_actor_body, headers = CASTING_DIRECTOR_AUTH_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

        test_actor_id = data["actor"]["id"]
        self.assertTrue(test_actor_id)
        test_actor = Actor.query.filter(Actor.id == test_actor_id).one_or_none()
        test_actor.delete()

    def test_post_movie_casting_director(self):
        test_movie_body = {
            "title": "Dummy",
            "release_date": "2022-01-15"
        }
        res = self.client().post("/movies", json=test_movie_body, headers = CASTING_DIRECTOR_AUTH_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"], False)

    def test_delete_movie_casting_director(self):
        # insert a test movie
        test_movie = Movie(
            title="Dummy",
            release_date = datetime.datetime(2000, 1, 1)
        )

        test_movie.insert()

        test_movie_id = Movie.query.filter(Movie.title == test_movie.title).one_or_none().id

        # delete question
        res = self.client().delete(
            "/movies/{}".format(test_movie_id),
            headers = CASTING_DIRECTOR_AUTH_HEADER
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"], False)

        test_movie.delete()
    

    ##### EXECUTIVE PRODUCER TESTS #####
    
    def test_retrieve_actors_executive_producer(self):
        res = self.client().get("/actors", headers = EXECUTIVE_PRODUCER_AUTH_HEADER)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["actors"])

    def test_retrieve_movies_executive_producer(self):
        res = self.client().get("/movies", headers = CASTING_DIRECTOR_AUTH_HEADER)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["movies"])

    def test_delete_movie_executive_producer(self):
        # insert a test movie
        test_movie = Movie(
            title="Dummy",
            release_date = datetime.datetime(2000, 1, 1)
        )

        test_movie.insert()

        test_movie_id = Movie.query.filter(Movie.title == test_movie.title).one_or_none().id

        # delete question
        res = self.client().delete(
            "/movies/{}".format(test_movie_id),
            headers = EXECUTIVE_PRODUCER_AUTH_HEADER
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_patch_actor_executive_producer(self):
        # insert a test actor
        test_actor = Actor(
            name="Dummy",
            gender="Male",
            age=25
        )

        test_actor.insert()

        test_actor_id = Actor.query.filter(Actor.name == test_actor.name).one_or_none().id

        updated_actor_body = {
            "name": "New Dummy",
            "age": 40
        }

        test_uri = "/actors/{}".format(test_actor_id)

        res = self.client().patch(test_uri, json=updated_actor_body, headers = EXECUTIVE_PRODUCER_AUTH_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["actor"]["name"], "New Dummy")
        self.assertEqual(data["actor"]["age"], 40)

        test_actor.delete()

    def test_patch_movie_executive_producer(self):
        # insert a test movie
        test_movie = Movie(
            title="Dummy",
            release_date=datetime.datetime(2000, 1, 1)
        )

        test_movie.insert()

        test_movie_id = Movie.query.filter(Movie.title == test_movie.title).one_or_none().id

        updated_movie_body = {
            "title": "New Dummy",
            "release_date": "2022-01-15"
        }

        test_uri = "/movies/{}".format(test_movie_id)

        res = self.client().patch(test_uri, json=updated_movie_body, headers = EXECUTIVE_PRODUCER_AUTH_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["movie"]["title"], "New Dummy")
        self.assertEqual(data["movie"]["release_date"], "Sat, 15 Jan 2022 00:00:00 GMT")

    def test_post_actor_executive_producer(self):
        test_actor_body = {
            "name": "Dummy",
            "age": 30,
            "gender": "Male"
        }
        res = self.client().post("/actors", json=test_actor_body, headers = EXECUTIVE_PRODUCER_AUTH_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

        test_actor_id = data["actor"]["id"]
        self.assertTrue(test_actor_id)
        test_actor = Actor.query.filter(Actor.id == test_actor_id).one_or_none()
        test_actor.delete()

    def test_post_movie_executive_producer(self):
        test_movie_body = {
            "title": "Dummy",
            "release_date": "2022-01-15"
        }
        res = self.client().post("/movies", json=test_movie_body, headers = EXECUTIVE_PRODUCER_AUTH_HEADER)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

        test_movie_id = data["movie"]["id"]
        self.assertTrue(test_movie_id)
        test_movie = Movie.query.filter(Movie.id == test_movie_id).one_or_none()
        test_movie.delete()


    ##### TESTS WITHOUT AUTHORIZATION #####

    def test_retrieve_actors_no_authorization(self):
        res = self.client().get("/actors")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)

    def test_retrieve_movies_no_authorization(self):
        res = self.client().get("/movies")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)

    def test_delete_actor_no_authorization(self):
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
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)

        test_actor.delete()

    def test_patch_actor_no_authorization(self):
        # insert a test actor
        test_actor = Actor(
            name="Dummy",
            gender="Male",
            age=25
        )

        test_actor.insert()

        test_actor_id = Actor.query.filter(Actor.name == test_actor.name).one_or_none().id

        updated_actor_body = {
            "name": "New Dummy",
            "age": 40
        }

        test_uri = "/actors/{}".format(test_actor_id)

        res = self.client().patch(test_uri, json=updated_actor_body)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)

        test_actor.delete()

    def test_patch_movie_no_authorization(self):
        # insert a test movie
        test_movie = Movie(
            title="Dummy",
            release_date=datetime.datetime(2000, 1, 1)
        )

        test_movie.insert()

        test_movie_id = Movie.query.filter(Movie.title == test_movie.title).one_or_none().id

        updated_movie_body = {
            "title": "New Dummy",
            "release_date": "2022-01-15"
        }

        test_uri = "/movies/{}".format(test_movie_id)

        res = self.client().patch(test_uri, json=updated_movie_body)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        
    def test_post_actor_no_authorization(self):
        test_actor_body = {
            "name": "Dummy",
            "age": 30,
            "gender": "Male"
        }
        res = self.client().post("/actors", json=test_actor_body)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
    
    def test_post_movie_no_authorization(self):
        test_movie_body = {
            "title": "Dummy",
            "release_date": "2022-01-15"
        }
        res = self.client().post("/movies", json=test_movie_body)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)

    def test_delete_movie_no_authorization(self):
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
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)

        test_movie.delete()

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()