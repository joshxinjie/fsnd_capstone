import os
import sys
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from auth import AuthError, requires_auth
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
  @requires_auth('get:actors')
  def get_actors(jwt):
    """
    Endpoint
    GET /actors
    - requires the '' permission
    - returns the actor.format() data representation

    Returns status code 200 and json {"success": True, "actors": formatted_actors} 
    where formatted_actors is the list of actors or appropriate status code 
    indicating reason for failure.

    Parameters
    ----------
    jwt:
      JSON Web token
    
    Returns
    -------
    json object with the keys:
    
    success:
      Whether the request is successful
    actors:
      The actor.format() data representation of the actors
    """
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
  @requires_auth('get:movies')
  def get_movies(jwt):
    """
    Endpoint
    GET /movies
    - requires the '' permission
    - returns the movie.format() data representation

    Returns status code 200 and json {"success": True, "movies": formatted_movies} 
    where formatted_movies is the list of movies or appropriate status code 
    indicating reason for failure.

    Parameters
    ----------
    jwt:
      JSON Web token
    
    Returns
    -------
    json object with the keys:
    
    success:
      Whether the request is successful
    movies:
      The movie.format() data representation of the movies
    """
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
  @requires_auth('delete:actors')
  def delete_actor(jwt, id):
    """
    Endpoint
    DELETE /actors/<id>
    - <id> is the existing model id
    - respond with a 404 error if <id> is not found
    - delete the corresponding row for <id>
    - require the '' permission
    
    Returns status code 200 and json {"success": True, "actorID": id} 
    where id is the id of the deleted record or appropriate status 
    code indicating reason for failure.
    Parameters
    ----------
    jwt:
      JSON Web token
    id:
      The actor id
    
    Returns
    -------
    json object with the keys
    
    success:
      Whether the request is successful
    actorID:
      ID of the deleted actor
    """
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
  @requires_auth('delete:movies')
  def delete_movie(jwt, id):
    """
    Endpoint
    DELETE /movies/<id>
    - <id> is the existing model id
    - respond with a 404 error if <id> is not found
    - delete the corresponding row for <id>
    - require the '' permission
    
    Returns status code 200 and json {"success": True, "movieID": id} 
    where id is the id of the deleted record or appropriate status 
    code indicating reason for failure.
    Parameters
    ----------
    jwt:
      JSON Web token
    id:
      The movie id
    
    Returns
    -------
    json object with the keys
    
    success:
      Whether the request is successful
    movieID:
      ID of the deleted movie
    """
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
  @requires_auth('patch:actors')
  def patch_actor(jwt, id):
    """
    Endpoint
    PATCH /actors/<id>
    - where <id> is the existing model id
    - respond with a 404 error if <id> is not found
    - respond with a 400 error if request body is missing 'name' and 'gender' and 'age'
    - update the corresponding row for <id>
    - require the '' permission
    - returns the actor.format() data representation
    
    Returns status code 200 and json {"success": True, "actor": actor} 
    where actor is a json containing only the updated actor or 
    appropriate status code indicating reason for failure.

    Parameters
    ----------
    jwt:
      JSON Web token
    id:
      The actor id
    
    Returns
    -------
    json object with the keys
    
    success:
      Whether the request is successful
    drinks:
      The actor.format() data representation of the updated actor
    """
    body = request.get_json()

    updated_name = None
    updated_gender = None
    updated_age = None

    if ("name" not in body) and ("gender" not in body) and ("age" not in body):
      abort(400)
    else:
      if "name" in body:
        updated_name = body["name"]
      if "gender" in body:
        updated_gender = body["gender"]
      if "age" in body:
        updated_age = body["age"]

    try:
        actor = Actor.query.filter(Actor.id == id).one_or_none()
        if actor is None:
          abort(404)
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
  @requires_auth('patch:movies')
  def patch_movie(jwt, id):
    """
    Endpoint
    PATCH /movies/<id>
    - where <id> is the existing model id
    - respond with a 404 error if <id> is not found
    - respond with a 400 error if request body is missing 'title' and 'release_date'
    - update the corresponding row for <id>
    - require the '' permission
    - returns the movie.format() data representation
    
    Returns status code 200 and json {"success": True, "movie": movie} 
    where movie is a json containing only the updated movie or 
    appropriate status code indicating reason for failure.

    Parameters
    ----------
    jwt:
      JSON Web token
    id:
      The movie id
    
    Returns
    -------
    json object with the keys
    
    success:
      Whether the request is successful
    drinks:
      The movie.format() data representation of the updated movie
    """
    body = request.get_json()

    updated_title = None
    updated_release_date = None

    if ("title" not in body) and ("release_date" not in body):
      abort(400)
    else:
      if "title" in body:
        updated_title = body["title"]
      if "release_date" in body:
        updated_release_date = body["release_date"]

    try:
        movie = Movie.query.filter(Movie.id == id).one_or_none()
        if updated_title:
            movie.title = updated_title
        if updated_release_date:
            movie.release_date = updated_release_date
        movie.update()
        return jsonify(
            {
              'success': True,
              'movie': movie.format()
            }
        )
    except:
        print(sys.exc_info())
        abort(422)

  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def post_actor(jwt):
    """
    Endpoint
    POST /actors
    - create a new row in the Actor table
    - request body must contain at least one of 'name' and 'gender' and 'age'
    - respond with a 400 error if request body does not contain 'name' and 'gender' and 'age'
    - require the '' permission
    - returns the actor.format() data representation
    
    Returns status code 200 and json {"success": True, "actor": new_actor} 
    where new_actor is a json containing only the newly created actor
    or appropriate status code indicating reason for failure.

    Parameters
    ----------
    jwt:
      JSON Web token
    
    Returns
    -------
    json object with the keys:
    
    success:
      Whether the request is successful
    actor:
      The actor.format() data representation of the new actor
    """
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
  @requires_auth('post:movies')
  def post_movie(jwt):
    """
    Endpoint
    POST /movies
    - create a new row in the Movie table
    - request body must contain at least one of 'title' and 'release_date'
    - respond with a 400 error if request body does not contain 'title' and 'release_date'
    - require the '' permission
    - returns the movie.format() data representation
    
    Returns status code 200 and json {"success": True, "movie": new_movie} 
    where new_movie is a json containing only the newly created movie
    or appropriate status code indicating reason for failure.

    Parameters
    ----------
    jwt:
      JSON Web token
    
    Returns
    -------
    json object with the keys:
    
    success:
      Whether the request is successful
    drink:
      The movie.format() data representation of the new movie
    """
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