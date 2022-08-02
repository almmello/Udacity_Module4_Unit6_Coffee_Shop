# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of Python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight SQLite database. 

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Used for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory, ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks Completed

### Auth0 setted

1. Created a new Auth0 tenant exclusively for demonstration.
3. Created a new, single-page web application
4. Created a new API with the following:
     - Enable RBAC
     - Enable Add Permissions in the Access Token
5. Created new API permissions:
   - `get:drinks`
   - `get:drinks-detail`
   - `post:drinks`
   - `patch:drinks`
   - `delete:drinks`
6. Created new roles for:
   - Barista
     - can `get:drinks-detail`
     - can `get:drinks`
   - Manager
     - can perform all actions
7. Tested with [Postman](https://getpostman.com).
   - Two users were created for testing. Barista role was assigned to one and the Manager role to the other.
   - A new postman collection, `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`, was updated into the repository with the new JWT in the token field.
   - Those JWT are set for maximum token_lifetime_for_web (86400), and they will expire on Aug the 3rd, 2022, 12:16:08 GMT-0300.
   
