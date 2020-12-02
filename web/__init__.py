
#
# python3 -m pip install --user --upgrade pip
# python3 -m pip install --user virtualenv
# create venv: python3 -m venv env
# source env/bin/activate

# FROM VIDEO:
# pipenv --python python3.9 install flask
# pipenv shell 
# pipenv install psycopg2-binary Flask-Migrate Flask-SQLAlchemy
# flask run --host=0.0.0.0 --port=3000

# Docker:
# dockerd
# sudo docker ps
# sudo docker exec -i postgres psql postgres -U pguser -c "CREATE DATABASE notes;"
# sudo docker exec -i postgres psql postgres -U pguser -c "ALTER USER pguser PASSWORD 'pgpassword';"

# Postgres:
# sudo systemctl start postgresql@13-main
# sudo systemctl enable postgresql@13-main
#
# sudo docker rm --force postgres
# sudo docker volume create pg-data
# sudo docker run --name postgres2 POSTGRES_USER=pguser -e POSTGRES_PASSWORD=pgpassword -d postgres -v "pg-data:/var/lib/postgresql/data" -e PGDATA=/var/lib/postgresql/data/pgdata
# 
# sudo docker volume create pg-data
# sudo docker run -d \
# --name postgres \
# -e POSTGRES_USER=pguser \
# -e POSTGRES_PASSWORD=pgpassword \
# -e POSTGRES_DB=notes \
# -e PGDATA=/var/lib/postgresql/data/pgdata \
# -v "pg-data:/var/lib/postgresql/data" \
# -p "5432:5432" \
# --restart always \
# postgres:13.1-alpine
#
# Connect to Postgres in Docker Container
# docker exec -it [container_name] psql -U [postgres_user] [db_name]
# docker exec -it postgres psql -U pguser notes
# 
# Connect to the database as the postgres user type:
# create database [db_name];
# \c [db_name]
# create schema [db_schema_name]
# create table [table_name] ([field_names] [values])
# 
# #psql -h localhost -p 5432 -U postgress testdb
####################
# postgres show tables: \dt
#
#
#
####################
# pipenv install --dev python-dotenv
# To activate this project's virtualenv, run pipenv shell.
# Alternatively, run a command inside the virtualenv with pipenv run.
#
# pipenv install psycopg2-binary Flask-SQLAlchemy Flask-Migrate
#
# flask db init
# flask db migrate
# flask db upgrade
# git log
# git status
# git add --all .
# git commit -m "miau"
# git push
#




import os
from flask import Flask
from flask_migrate import Migrate

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY=os.environ.get('SECRET_KEY', default='dev'))
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    from .models import db
    db.init_app(app)
    migrate = Migrate(app,db)
        
    return app




