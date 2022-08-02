# Coffee Shop Full Stack

## My Release

This repository is my version of the Coffee Shop app (https://github.com/udacity/cd0039-Identity-and-Access-Management/tree/master/Project/03_coffee_shop_full_stack/starter_code).
I recorded my development through commits so that you can follow along.

Please let me know if you find any issues with this project.


## References

During the development, I used the following references to build the Coffee Shop app:

https://learn.udacity.com/nanodegrees/nd0044/
https://flask-wtf.readthedocs.io/en/1.0.x/
https://flask.palletsprojects.com/en/2.1.x/
https://flask.palletsprojects.com/en/2.1.x/patterns/packages/
https://flask.palletsprojects.com/en/1.0.x/patterns/flashing/
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#
https://flask-moment.readthedocs.io/en/latest/quickstart.html#installation-and-configuration
https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
https://www.linkedin.com/learning/full-stack-web-development-with-flask/
https://flask.palletsprojects.com/en/1.1.x/errorhandling/#generic-exception-handlers
https://auth0.com/docs
https://community.auth0.com/t/whats-the-limit-for-api-token-expiration-for-browser-flows-seconds/6862
https://jwt.io/




## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard.

### Achievements

I have created a full-stack drink menu application. With the following functionalities:

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.

### Stack Separation

There are separate docs for the backend and frontend. Please read each one of them after reading this file.

1. [`./backend/`](./backend/README.md)
2. [`./frontend/`](./frontend/README.md)

### Backend

The `./backend` directory contains a Flask server with an SQLAlchemy module to supply your data needs. 

The endpoints are configured and integrated with Auth0 for authentication.

### Frontend

The `./frontend` directory contains a complete Ionic frontend to consume the data from the Flask server.
In 
The environment variables (./frontend/src/environment/environment.ts) reflect the Auth0 configuration details for the backend app.

