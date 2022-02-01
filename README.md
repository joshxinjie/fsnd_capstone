# Full Stack Nanodegree Capstone

Heroku App URL: `https://fsnd-capstone-xj.herokuapp.com/`

---

## A. Project Background and Motivation 
This is the capstone project for the Udacity Full Stack Engineering Nanodegree. It concerns a Casting Agency company that is responsible for creating movies and managing and assigning actors to those movies.

The following specifications are implemented.

Models:

    Movies with attributes title and release date
    Actors with attributes name, age and gender

Endpoints:

    GET /actors and /movies
    DELETE /actors/ and /movies/
    POST /actors and /movies and
    PATCH /actors/ and /movies/

Roles:

    Casting Assistant
        Can view actors and movies
    Casting Director
        All permissions a Casting Assistant has and…
        Add or delete an actor from the database
        Modify actors or movies
    Executive Producer
        All permissions a Casting Director has and…
        Add or delete a movie from the database


---


## B. Local Setup of Virtual Environment

Create a virtual environment `fsndcapstone`:
```
python3 -m virtualenv fsndcapstone
```

Activate the virtual environment `fsndcapstone`:
```
source fsndcapstone/bin/activate
```

Install requirements
```
pip install -r requirements.txt
```


---


## C. Run Local Development Server

```
export FLASK_APP=app
export FLASK_ENV=development # enables debug mode
python3 app.py
```

The local app will be hosted at http://127.0.0.1:8080/


---


## D. Run Tests Locally

### 1. Create `.env` file
Create a `.env` file to store the bearer tokens obtained after all users (casting assistant, casting director, executive producer) have logged on, e.g.
```
CASTING_ASSISTANT_TOKEN="Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhQcnFjMjlycERFLW1FeUJjNDc2QSJ9.eyJpc3MiOiJodHRwczovL2Rldi03bDA0cnJuZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFmNGYyNjBmMjcwNWEwMDY4NTJiMjUyIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTY0MzYxNTU1NiwiZXhwIjoxNjQzNjIyNzU2LCJhenAiOiJUdXFIZjNFb1FHWWprRXRKRDVYVjhvTWZKSGpXTktuNSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.kWCaK70FIIqS42GPdRnu9N_NWgi4x01KDuWL3Gl71soIVvAzUBqwcyGHWO_O_q6WtSpt-aTRL_aX225uXf0V4eeozIqB3re7FtpZIFYszMpG_BZHTouBS09Ra-nDqfpY0CoK_JyazoKMNkxIyFDcjxDqON2WTCZi3YtPUF6lG1GVj8w946KqBLv_n6ycG8g5RZ-RSMIBQnKDyPtQvk0cp0VrfKIT9gZlwmCjesk7igbRX_S0u66-8GXQwJcDxBDctYpBoSOlCuuWFw9gSiOwewD28DFVTlb7kqksanT4Ox_G04ojqXh_0-Oeo4eNHXa7yb8-8dyx4HLfNiRXOiXMcw"

CASTING_DIRECTOR_TOKEN="Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhQcnFjMjlycERFLW1FeUJjNDc2QSJ9.eyJpc3MiOiJodHRwczovL2Rldi03bDA0cnJuZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFmNjI5YjVmMjcwNWEwMDY4NTJjZTkxIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTY0MzYxNDA1MSwiZXhwIjoxNjQzNjIxMjUxLCJhenAiOiJUdXFIZjNFb1FHWWprRXRKRDVYVjhvTWZKSGpXTktuNSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.sZsothZyp2i1lun_x9xM1EG7TY_NPuwIZbkm2IJcSqlJi4T7VjHuIQUcRUPvnlYzo1Rzpl3YiZ_Un-TqctetzoniLMqaEc2iNPP9EnPk-a1nhzOgFM_Nxad1fJK4nrGvjdoltk_98SatpdGUlkBegDnX4OwkYmFfGs6AY6l0VhbalTJPN2usyX7Ia7bODYjXBawAemwkGJEadhPbWwXDX1YIJEQJSBA6GxCdsK4WG-JPbI17xsQl3MF5Wgc86OWg9Q54iVBvMiyekanQaVx3Oj0xmwdWDzIlk6qo_iWCaV5g0XsRhFasHt8qCns0BL5CUagSHC-4Kl2nkQ4SNncqgQ"

EXECUTIVE_PRODUCER_TOKEN="Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhQcnFjMjlycERFLW1FeUJjNDc2QSJ9.eyJpc3MiOiJodHRwczovL2Rldi03bDA0cnJuZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFmNjJhZWFiZDQ5NGUwMDcwNjU4ZGIyIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTY0MzYxNDExMSwiZXhwIjoxNjQzNjIxMzExLCJhenAiOiJUdXFIZjNFb1FHWWprRXRKRDVYVjhvTWZKSGpXTktuNSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.LrHc6TUjNflTUhK0vJ6QSGiWJuEw1M9MxT1cPJS1URblOfsLsuzurFiColGDXjSXZBt_pkfdjkW9IJOPrl16zM0rkoIdApekX51cLaDDhL7nvip55dt3mGsGd-LvMmG2BJqFC99WGAMnvCID1-CD1xkB8XmPMdAcB1Z2yyRYWWDn6Jr7NDJcmWRFXtDMFL4fLyzhJlfWNkdWMPN4cWRQY1TdxKVQ0rLho0SaSEdBddR5UWbu3ldkaNSP_BPWd3QalV8XAeiei21T8_YD6XQDbHWPEzRAWhY-r36oF7cSPMoWBjSKjBPWoPAJPfMUKGz854LbdJMPmSO4dxGAOmJiAg"
```

### 2. Run the tests
```
python -m test_app
```


---

## E. Auth0 Authentication Setup

The third-party authentication service Auth0 is used to manage authentication.

1. Log onto https://manage.auth0.com

2. Go the the `Applications` tab, create a new application by clicking `+ Create Application`. Choose `Regular Web Applications`. The name used for this application is `CastingService`.

3. Update `AUTH0_DOMAIN` and `API_AUDIENCE` in `auth.py` using the information from `Settings` page in the `CastingService` applications page.

4. Fill in the `Allowed Callback URLs`, e.g. `http://127.0.0.1:8080/login-results`. Click the `Save Changes` button at the bottom of the page to save the changes.

5. Go to the `APIs` tab, create a new API by selecting `+ Create API`. The name and identifier used for this application are both `Casting`.

6. Update `API_AUDIENCE` in `auth.py` using the information from `Settings` page in the `Casting` API page.

7. Enable both options in the `Settings` page of the `Casting` API page: `Enable RBAC` and `Add Permissions in the Access Token`. Click the `Save` button at the bottom to save the new settings.

8. Go to `User Management`, then `Roles`. Click on `+ Create Role`, and create the `Casting Assistant` role. Add a description for the role.

9. Repeat the role creation for `Casting Director` and `Executive Producer`.

10. Return to the `Casting` API page, then select `Permissions`. Create the following permissions and add the appropriate descriptions for each role:
```
get:actors
get:movies
post:actors
delete:actors
patch:actors
patch:movies
post:movies
delete:movies
```

11. Return to `User Management`, then `Roles`. Assign the appropriate permissions to each role.
```
Casting Assistant
  get:actors
  get:movies

Casting Director
  get:actors
  get:movies
  post:actors
  delete:actors
  patch:actors
  patch:movies

Executive Producer
  get:actors
  get:movies
  post:actors
  delete:actors
  patch:actors
  patch:movies
  post:movies
  delete:movies
```

12. When the users create their accounts, assign each user their appropriate role under the `User Management` tab, then `Users` page.


---


## F. Heroku Deployment Instructions

### 1. Create a Heroku app

```
heroku create name_of_your_app

# Example
heroku create fsnd-capstone-xj
```

This returns a git url for your Heroku application, which you will need in a moment.
```
 ›   Warning: heroku update available from 7.59.0 to 7.59.2.
Creating ⬢ fsnd-capstone-xj... done
https://fsnd-capstone-xj.herokuapp.com/ | https://git.heroku.com/fsnd-capstone-xj.git
```

### 2. Add git remote for Heroku to local repository

If repository is new, run the following command in the terminal using the git url obtained from the last step:
```
git remote add heroku heroku_git_url

# Example
git remote add heroku https://git.heroku.com/fsnd-capstone-xj.git
```

or

If you are linking an existing repo to the heroku app for the first time:
```
heroku git:remote -a name_of_your_application

# Example
heroku git:remote -a fsnd-capstone-xj
```

A sample output:
```
 ›   Warning: heroku update available from 7.59.0 to 7.59.2.
set git remote heroku to https://git.heroku.com/fsnd-capstone-xj.git
```

### 3. Add postgresql add on for our database

Heroku has an addon for apps for a postgresql database instance. Run this code in order to create your database and connect it to your application:

```
heroku addons:create heroku-postgresql:hobby-dev --app name_of_your_application

# Example
heroku addons:create heroku-postgresql:hobby-dev --app fsnd-capstone-xj
```

A sample output:
```
 ›   Warning: heroku update available from 7.59.0 to 7.59.2.
Creating heroku-postgresql:hobby-dev on ⬢ fsnd-capstone-xj... free
Database has been created and is available
 ! This database is empty. If upgrading, you can transfer
 ! data from another database with pg:copy
Created postgresql-shaped-85638 as DATABASE_URL
Use heroku addons:docs heroku-postgresql to view documentation
```

Breaking down the heroku-postgresql:hobby-dev section of this command, heroku-postgresql is the name of the addon. hobby-dev on the other hand specifies the tier of the addon, in this case the free version which has a limit on the amount of data it will store, albeit fairly high.

Run `heroku config --app name_of_your_application` in order to check your configuration variables in Heroku. You will see DATABASE_URL and the URL of the database you just created.
```
heroku config --app name_of_your_application

# Example
heroku config --app fsnd-capstone-xj
```

A sample output:
```
 ›   Warning: heroku update available from 7.59.0 to 7.59.2.
=== fsnd-capstone-xj Config Vars
DATABASE_URL: postgres://focudljubvikoc:58c505f1eb03c923464800a25a01211d7a352c026eaa6fbea27348383976bb9b@ec2-50-19-32-96.compute-1.amazonaws.com:5432/d2b7s41ijh0mbb
```

### 4. Commit changes and push them

```
git add .
git commit -am "make it better"

# If pushing from Git master branch to Heroku master branch
git push heroku master
#Or
# If pushing from Git main branch to Heroku master branch
git push heroku main:master
```

### 5. Virtual environment (If necessary)

Create and activate the virtual environment locally if this step has not been performed.

```
python3 -m virtualenv fsndcapstone
source fsndcapstone/bin/activate
pip install -r requirements.txt
```

### 6. Update config.py with Heroku Database URI

Update `HEROKU_SQLALCHEMY_DATABASE_URI` in config.py with the Heroku postgresql database URL:
```
HEROKU_SQLALCHEMY_DATABASE_URI="postgresql://focudljubvikoc:58c505f1eb03c923464800a25a01211d7a352c026eaa6fbea27348383976bb9b@ec2-50-19-32-96.compute-1.amazonaws.com:5432/d2b7s41ijh0mbb"
```

Ensure `DEPLOYMENT` is set to `"heroku"`.
```
DEPLOYMENT="heroku"
```

### 7. Initialise migrations locally:

If the following steps has not been performed, e.g. migrations/versions folder has not been created yet, run:

```
flask db init
flask db migrate
```

Add a .gitkeep file in /migrations/versions to commit the empty folder /migrations/versions.

### 8. Add and push to Heroku

```
git add .
git commit -am "add migrations folder"

# If pushing from Git master branch to Heroku master branch
git push heroku master
#Or
# If pushing from Git main branch to Heroku master branch
git push heroku main:master
```

### 9. Run migrations on Heroku

Once your app is deployed, run migrations by running:
```
heroku run python manage.py db upgrade --app name_of_your_application

# Example
heroku run python manage.py db upgrade --app fsnd-capstone-xj
```

A sample output:
```
 ›   Warning: heroku update available from 7.59.0 to 7.59.2.
Running python manage.py db upgrade on ⬢ fsnd-capstone-xj... up, run.5655 (Free)
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
```


---


## G. API Reference

### Getting Started
- Base URL: `https://fsnd-capstone-xj.herokuapp.com/`
- Authentication: Managed by Auth0. Log on or create an account using the following URL https://dev-7l04rrne.us.auth0.com/authorize?audience=casting&response_type=token&client_id=TuqHf3EoQGYjkEtJD5XV8oMfJHjWNKn5&redirect_uri=http://127.0.0.1:8080/login-results


### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```

The API will return three error types when requests fail:
```
    400: `Bad Request` or `Unable to parse authentication token` or `Unable to find the appropriate key` or `Permissions not included in JWT`
    401: `Token expired` or `Incorrect claims. Please, check the audience and issuer` or `Authorization malformed` or `Permissions not found` or `Authorization header is expected` or `Authorization header must start with "Bearer` or `Token not found` or `Authorization header must be bearer token`
    403: `Unauthorized`
    404: `Resource Not Found`
    422: `Not Processable`
```

### Notes

To successfully invoke the endpoints, you need to attach the bearer token with your CURL requests. To obtain the bearer token, logon to the application using the [URL](https://dev-7l04rrne.us.auth0.com/authorize?audience=casting&response_type=token&client_id=TuqHf3EoQGYjkEtJD5XV8oMfJHjWNKn5&redirect_uri=http://127.0.0.1:8080/login-results)

Obtain the bearer token from the URL after logging in. For example in the forwarded URL:
```
http://127.0.0.1:8080/login-results#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhQcnFjMjlycERFLW1FeUJjNDc2QSJ9.eyJpc3MiOiJodHRwczovL2Rldi03bDA0cnJuZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFmNGYyNjBmMjcwNWEwMDY4NTJiMjUyIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTY0MzcwMTk0NiwiZXhwIjoxNjQzNzA5MTQ2LCJhenAiOiJUdXFIZjNFb1FHWWprRXRKRDVYVjhvTWZKSGpXTktuNSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.t1_y_qvl2NB8w6H7nm1SQBZycVq12OewEdAbez9iUdOVznuOFsVO4nAmk-j_A43ByA2S2Z_dx6BlqnfxqONuBpmhV-JForgWwk7fHJ2SW2mJ05t985zyeNZUVgVx2n3shlUvHfldWnV9EsL4m-c9FUIk1MwMLOrSnSlBxyJ1wQ-ZJ7GVP8l2nE_c-Q4_4VAvnhoH4Wbnm625IQ3LhwK_Gg8B-L2eirooTpMpotx-JHU-MxTFDw9rGf0M5b4KR7cj8q-2FSDWQsJUbZ3lRaIiX20Kyftd28ZviM8CNbyQq9LblUncAtegG5xReFkysw7cZb0FaaN-RcAilFLgVMwZGw&expires_in=7200&token_type=Bearer
```

The bearer token will be:
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhQcnFjMjlycERFLW1FeUJjNDc2QSJ9.eyJpc3MiOiJodHRwczovL2Rldi03bDA0cnJuZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFmNGYyNjBmMjcwNWEwMDY4NTJiMjUyIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTY0MzcwMTk0NiwiZXhwIjoxNjQzNzA5MTQ2LCJhenAiOiJUdXFIZjNFb1FHWWprRXRKRDVYVjhvTWZKSGpXTktuNSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.t1_y_qvl2NB8w6H7nm1SQBZycVq12OewEdAbez9iUdOVznuOFsVO4nAmk-j_A43ByA2S2Z_dx6BlqnfxqONuBpmhV-JForgWwk7fHJ2SW2mJ05t985zyeNZUVgVx2n3shlUvHfldWnV9EsL4m-c9FUIk1MwMLOrSnSlBxyJ1wQ-ZJ7GVP8l2nE_c-Q4_4VAvnhoH4Wbnm625IQ3LhwK_Gg8B-L2eirooTpMpotx-JHU-MxTFDw9rGf0M5b4KR7cj8q-2FSDWQsJUbZ3lRaIiX20Kyftd28ZviM8CNbyQq9LblUncAtegG5xReFkysw7cZb0FaaN-RcAilFLgVMwZGw
```

Export the bearer tokens in the terminal before running any CURL commands, e.g.:
```
export BEARER_TOKEN="Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhQcnFjMjlycERFLW1FeUJjNDc2QSJ9.eyJpc3MiOiJodHRwczovL2Rldi03bDA0cnJuZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFmNGYyNjBmMjcwNWEwMDY4NTJiMjUyIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTY0MzcwMTk0NiwiZXhwIjoxNjQzNzA5MTQ2LCJhenAiOiJUdXFIZjNFb1FHWWprRXRKRDVYVjhvTWZKSGpXTktuNSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.t1_y_qvl2NB8w6H7nm1SQBZycVq12OewEdAbez9iUdOVznuOFsVO4nAmk-j_A43ByA2S2Z_dx6BlqnfxqONuBpmhV-JForgWwk7fHJ2SW2mJ05t985zyeNZUVgVx2n3shlUvHfldWnV9EsL4m-c9FUIk1MwMLOrSnSlBxyJ1wQ-ZJ7GVP8l2nE_c-Q4_4VAvnhoH4Wbnm625IQ3LhwK_Gg8B-L2eirooTpMpotx-JHU-MxTFDw9rGf0M5b4KR7cj8q-2FSDWQsJUbZ3lRaIiX20Kyftd28ZviM8CNbyQq9LblUncAtegG5xReFkysw7cZb0FaaN-RcAilFLgVMwZGw"
```

We will use the environment variable `BEARER_TOKEN` for all endpoint examples. You may change the variable name where appropriate.

### Endpoints

#### 1. GET /actors
- General:
  - Returns a list of actors.
- Request Parameters: None
- Request Headers: None
- Sample:
  - `curl --header "Authorization: $BEARER_TOKEN" https://fsnd-capstone-xj.herokuapp.com/actors`
  - `curl --header "Authorization: $BEARER_TOKEN" http://127.0.0.1:8080/actors`

```
{
  "actors": [
    {
      "age": 25,
      "gender": "Male",
      "id": 1,
      "name": "Leonardo DiCaprio"
    },
    {
      "age": 25,
      "gender": "Female",
      "id": 2,
      "name": "Kate Winslet"
    },
  ],
  "success": true
}
```

#### 2. GET /movies
- General:
  - Returns a list of movies.
- Request Parameters: None
- Request Headers: None
- Sample:
  - `curl --header "Authorization: $BEARER_TOKEN" https://fsnd-capstone-xj.herokuapp.com/movies`
  - `curl --header "Authorization: $BEARER_TOKEN" http://127.0.0.1:8080/movies`

```
{
  "movies": [
    {
      "id": 1,
      "release_date": "Fri, 19 Dec 1997 00:00:00 GMT",
      "title": "Titanic"
    },
    {
      "id": 2,
      "release_date": "Fri, 18 Dec 2009 00:00:00 GMT",
      "title": "Avatar"
    }
  ],
  "success": true
}
```

#### 3. DELETE /actors/{id}
- General:
  - Deletes the actor of the given ID if it exists. Returns the id of the deleted actor, success value.
- Request Parameters:
  - `id` Integer
- Request Headers: None
- Sample:
  - `curl --header "Authorization: $BEARER_TOKEN" -X DELETE https://fsnd-capstone-xj.herokuapp.com/actors/12`
  - `curl --header "Authorization: $BEARER_TOKEN" -X DELETE http://127.0.0.1:8080/actors/12`

```
{
  "actorID": "12",
  "success": true
}
```

#### 4. DELETE /movies/{id}
- General:
  - Deletes the movie of the given ID if it exists. Returns the id of the deleted movie, success value.
- Request Parameters:
  - `id` Integer
- Request Headers: None
- Sample:
  - `curl --header "Authorization: $BEARER_TOKEN" -X DELETE https://fsnd-capstone-xj.herokuapp.com/movies/12`
  - `curl --header "Authorization: $BEARER_TOKEN" -X DELETE http://127.0.0.1:8080/movies/12`

```
{
  "movieID": "12",
  "success": true
}
```

#### 5. PATCH /actors/{id}
- General:
  - Edits the actor of the given ID if it exists. Returns the updated actor information and success value.
- Request Parameters:
  - `id` Integer
- Request Headers:
  - JSON
    - `name` String
    - `age` Integer
    - `gender` String
- Sample:
  - `curl --header "Authorization: $BEARER_TOKEN" https://fsnd-capstone-xj.herokuapp.com/actors/11 -X PATCH -H "Content-Type: application/json" -d '{"name": "Updated Name", "age":40}'`
    - `curl --header "Authorization: $BEARER_TOKEN" http://127.0.0.1:8080/actors/11 -X PATCH -H "Content-Type: application/json" -d '{"name": "Updated Name", "age":40}'`

```
{
  "actor": {
    "age": 40,
    "gender": "Male",
    "id": 11,
    "name": "Updated Name"
  },
  "success": true
}
```

#### 6. PATCH /movies/{id}
- General:
  - Edits the movie of the given ID if it exists. Returns the updated movie information and success value.
- Request Parameters:
  - `id` Integer
- Request Headers:
  - JSON
    - `title` String 
    - `release_date` Datetime
- Sample:
  - `curl --header "Authorization: $BEARER_TOKEN" https://fsnd-capstone-xj.herokuapp.com/movies/11 -X PATCH -H "Content-Type: application/json" -d '{"title": "Updated Title", "release_date":"2022-01-15"}'`
    - `curl --header "Authorization: $BEARER_TOKEN" http://127.0.0.1:8080/movies/11 -X PATCH -H "Content-Type: application/json" -d '{"title": "Updated Title", "release_date":"2022-01-15"}'`

```
{
  "movie": {
    "id": 11,
    "release_date": "Sat, 15 Jan 2022 00:00:00 GMT",
    "title": "Updated Title"
  },
  "success": true
}
```

#### 7. POST /actors
- General:
  - Adds a new actor. Returns the actor information and success value.
- Request Parameters: None
- Request Headers:
  - JSON
    - `name` String
    - `age` Integer
    - `gender` String
- Sample:
  - `curl --header "Authorization: $BEARER_TOKEN" https://fsnd-capstone-xj.herokuapp.com/actors -X POST -H "Content-Type: application/json" -d '{"name": "New Name", "age":40, "gender":"Male"}'`
    - `curl --header "Authorization: $BEARER_TOKEN" http://127.0.0.1:8080/actors -X POST -H "Content-Type: application/json" -d '{"name": "New Name", "age":40, "gender":"Male"}'`

```
{
  "actor":{
    "age":40,
    "gender":"Male",
    "id":13,
    "name":"New Name"
  },
  "success":true
}
```

#### 8. POST /movies
- General:
  - Adds a new movies. Returns the movie information and success value.
- Request Parameters: None
- Request Headers:
  - JSON
    - `title` String
    - `release_date` Datetime
- Sample:
  - `curl --header "Authorization: $BEARER_TOKEN" https://fsnd-capstone-xj.herokuapp.com/movies -X POST -H "Content-Type: application/json" -d '{"title": "New Title", "release_date":"2022-01-15"}'`
    - `curl --header "Authorization: $BEARER_TOKEN" http://127.0.0.1:8080/movies -X POST -H "Content-Type: application/json" -d '{"title": "New Title", "release_date":"2022-01-15"}'`

```
{
  "movie": {
    "id": 13,
    "release_date": "Sat, 15 Jan 2022 00:00:00 GMT",
    "title": "New Title"
  },
  "success": true
}
```