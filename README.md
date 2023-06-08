# Spot FastAPI App

## Without using docker
You have to create the database with the credentials that appear in the environment variables file (dev.env)

```

pip install -r requirements.txt

vunicorn app.main:app --host=0.0.0.0 --reload --env-file=dev.env

```

## Using docker
The following must be run to build and run the container. It is not necessary to create the postgres database, as it is created within the same container automatically:

```

sudo docker-compose up -d --build

```

### To open the application you must go to the url http://127.0.0.1:8000/docs
