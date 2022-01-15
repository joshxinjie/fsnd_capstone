import os
import sys
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Movie, Actor, db_drop_and_create_all, db_init_sample_records
from config import DEPLOYMENT, LOCAL_SQLALCHEMY_DATABASE_URI, HEROKU_SQLALCHEMY_DATABASE_URI

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)

  if DEPLOYMENT=="local":
    database_uri = LOCAL_SQLALCHEMY_DATABASE_URI
  elif DEPLOYMENT=="heroku":
    database_uri = HEROKU_SQLALCHEMY_DATABASE_URI
  else:
    raise NotImplementedError("Deployment mode not implemented. Use 'local' or 'heroku'.")

  setup_db(
    app=app,\
    database_uri=database_uri
  )

  db_drop_and_create_all()
  db_init_sample_records()

  CORS(app, resources={r"/api/*": {"origins": "*"}})

  # CORS Headers
  @app.after_request
  def after_request(response):
    response.headers.add(
      "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
    )
    response.headers.add(
      "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
    )
    return response

  @app.route('/actors', methods=['GET'])
  def get_actors():
    actors = Actor.query.order_by(Actor.id).all()
    formatted_actors = [actor.format() for actor in actors]
    
    if len(formatted_actors) == 0:
          abort(404)

    return jsonify(
      {
        "success": True,
        "actors": formatted_actors
      }
    )

  @app.route('/movies', methods=['GET'])
  def get_movies():
    movies = Movie.query.order_by(Movie.id).all()
    formatted_movies = [movie.format() for movie in movies]
    
    if len(formatted_movies) == 0:
          abort(404)

    return jsonify(
      {
        "success": True,
        "movies": formatted_movies
      }
    )

  @app.route('/actors/<id>', methods=['DELETE'])
  def delete_actor(id):
    actor = Actor.query.filter(Actor.id == id).one_or_none()

    if actor is None:
      abort(404)

    try:
      actor.delete()

      return jsonify(
        {
          'success': True,
          'actorID': id
        }
      )
    except:
      print(sys.exc_info())
      abort(422)

  @app.route('/movies/<id>', methods=['DELETE'])
  def delete_movie(id):
    movie = Movie.query.filter(Movie.id == id).one_or_none()

    if movie is None:
      abort(404)

    try:
      movie.delete()

      return jsonify(
        {
          'success': True,
          'movieID': id
        }
      )
    except:
      print(sys.exc_info())
      abort(422)

  @app.route('/actors/<id>', methods=['PATCH'])
  def patch_actor(id):
    body = request.get_json()

    if ("name" in body) and ("gender" in body) and ("age" in body):
      updated_name = body["name"]
      updated_gender = body["gender"]
      updated_age = body["age"]
    else:
      abort(400)

    try:
        actor = Actor.query.filter(Actor.id == id).one_or_none()
        if updated_name:
            actor.name = updated_name
        if updated_gender:
            actor.gender = updated_gender
        if updated_age:
          actor.age = updated_age
        actor.update()
        return jsonify(
            {
                'success': True,
                'actor': actor.format()
            }
        )
    except:
        print(sys.exc_info())
        abort(422)

  @app.route('/movies/<id>', methods=['PATCH'])
  def patch_movie(id):
    pass

  @app.route('/actors', methods=['POST'])
  def post_actor():
    body = request.get_json()

    if ("name" in body) and ("gender" in body) and ("age" in body):
      name = body["name"]
      gender = body["gender"]
      age = body["age"]
    else:
      abort(400)

    try:
        new_actor = Actor(name = name, gender = gender, age=age)
        new_actor.insert()
        return jsonify(
          {
            'success': True,
            'actor': new_actor.format()
          }
        )
    except:
        print(sys.exc_info())
        abort(422)
    

  @app.route('/movies', methods=['POST'])
  def post_movie():
    body = request.get_json()

    if ("title" in body) and ("release_date" in body):
      title = body["title"]
      release_date = body["release_date"]
    else:
      abort(400)

    try:
        new_movie = Movie(title = title, release_date=release_date)
        new_movie.insert()
        return jsonify(
          {
            'success': True,
            'movie': new_movie.format()
          }
        )
    except:
        print(sys.exc_info())
        abort(422)

  return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)