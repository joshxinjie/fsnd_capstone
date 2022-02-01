# Full Stack Nanodegree Capstone

Heroku App URL: ``

## Background


## Setup Virtual Environment

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

## Run Local Development Server

```
export FLASK_APP=app
export FLASK_ENV=development # enables debug mode
python3 app.py
```

http://127.0.0.1:8080/

## Sample CURL Calls

```
curl http://127.0.0.1:8080/movies
```

returns
```
{
  "actors": [
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


```
curl http://127.0.0.1:8080/movies -X POST -H "Content-Type: application/json" -d '{"title": "Dummy", "release_date": "2022-01-15"}'
```

returns:
```
{
  "movie": {
    "id": 3, 
    "release_date": "Sat, 15 Jan 2022 00:00:00 GMT", 
    "title": "Dummy"
  }, 
  "success": true
}
```

## Run Tests Locally

```
python -m test_app
```

## Authentication

Auth0

To log on locally, go to the URL `https://dev-7l04rrne.us.auth0.com/authorize?audience=casting&response_type=token&client_id=TuqHf3EoQGYjkEtJD5XV8oMfJHjWNKn5&redirect_uri=http://127.0.0.1:8080/login-results`


To log on to the heroku app, go to the URL `https://dev-7l04rrne.us.auth0.com/authorize?audience=casting&response_type=token&client_id=TuqHf3EoQGYjkEtJD5XV8oMfJHjWNKn5&redirect_uri={REPLACE}/login-results`


## Heroku Setup

1. Create a Heroku app

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

2. Add git remote for Heroku to local repository

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

3. Add postgresql add on for our database

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

4. Commit changes and push them

```
git add .
git commit -am "make it better"

# If pushing from Git master branch to Heroku master branch
git push heroku master
#Or
# If pushing from Git main branch to Heroku master branch
git push heroku main:master
```

5. Virtual Environment (If necessary)

Create and activate the virtual environment if this step has not been performed.

```
python3 -m virtualenv fsndcapstone
source fsndcapstone/bin/activate
pip install -r requirements.txt
```

6. Export the DATABASE_URL:
```
export DATABASE_URL=
```

7. Initialise migrations locally (If necessary):

If the following steps has not been performed, e.g. migrations/versions folder has not been created yet, run:

```
flask db init
flask db migrate
```

Add a .gitkeep file in /migrations/versions to commit the empty folder /migrations/versions.

8. Add and push to Heroku

```
git add .
git commit -am "add migrations folder"

# If pushing from Git master branch to Heroku master branch
git push heroku master
#Or
# If pushing from Git main branch to Heroku master branch
git push heroku main:master
```

9. Run migrations on Heroku

Once your app is deployed, run migrations by running:
```
heroku run python manage.py db upgrade --app name_of_your_application

# Example
heroku run python manage.py db upgrade --app fsnd-capstone-xj
```

A sample output:
```
```