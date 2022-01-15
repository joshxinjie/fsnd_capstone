# fsnd_capstone

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