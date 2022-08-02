import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@OK uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one
'''
# db_drop_and_create_all()

# ROUTES
'''
@OK implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks', methods=['GET'], endpoint='get_drinks')
@requires_auth('get:drinks')
def read_all_drinks(jwt):

    # using the try-except method to create the query
    try:

        # create the query questions order by id
        query_drinks = Drink.query.all()

        # check if the query has no results and abort
        if len(query_drinks) == 0:
            abort(404)

        # if has results, return them
        else:

            return jsonify({
                'success': True,
                'drinks': [drink.short() for drink in query_drinks]
            })

    # if the query fails, abort
    except:
        abort(404)

'''
@OK implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks-detail', methods=['GET'], endpoint='drinks_detail')
@requires_auth('get:drinks-detail')
def read_all_drinks_detail(jwt):

    # using the try-except method to create the query
    try:

        # create the query drinks
        query_drinks = Drink.query.all()

        # check if the query has no results and abort
        if len(query_drinks) == 0:
            abort(404)

        # if has results, return them
        else:


            return jsonify({
                'success': True,
                'drinks': [drink.long() for drink in query_drinks]
            })

    # if the query fails, abort
    except:
        abort(404)

'''
@OK implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks', methods=['POST'], endpoint='post_drink')
@requires_auth('post:drinks')
def create_drink(jwt):

    # create the data JSON object
    data = request.get_json()

    # use the try-except method to insert the data
    try:
        new_drink = Drink(
            title=data.get('title'),
            recipe=json.dumps(data.get('recipe'))
        )

        new_drink.insert()

        # return the data
        return jsonify({
            'success': True,
            'drink': new_drink.long(),

        })

    # if insert fails, abort
    except:
        abort(400)


'''
@OK implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(jwt, id):

    # retrieve data from request to update the drink
    data = request.get_json()
    id_update = int(id)
    title_update=data.get('title'),
    recipe_update=json.dumps(data.get('recipe'))

    # use the try-except method to insert the data
    try:

        # create the query drink using requested id
        query_drink = Drink.query.get(id_update)

        # update query title and recipe
        query_drink.title = title_update[0]
        query_drink.recipe = recipe_update

        # if the query drink is not empty, update the drink
        if query_drink is not None:

            query_drink.update()

            # return the JSON object with the long drink
            return jsonify({
                'success': True,
                'drink': [query_drink.long()]
            })

        # if there are no results, abort
        else:
            abort(404)

    # if the query fails, abort
    except:
        abort(422)

'''
@OK implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(jwt, id):

    # using the try-except method to delete the drink
    try:

        # create the query drinks with the the id
        query_drinks = Drink.query.get(id)

        # if the drink is not empty, delete the drink
        if query_drinks is not None:
            query_drinks.delete()

            # return the JSON object with the long drink
            return jsonify({
                'success': True,
                'delete': id
            })

        # if the quere is empty, abort
        else:
            abort(404)

    # if the query fails, abort
    except Exception:
        abort(404)

# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
@OK implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@OK implement error handler for 404
    error handler should conform to general task above
'''

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
         "error": 404,
         "message": "resource not found"
    }), 404


'''
@OK implement error handler for AuthError
    error handler should conform to general task above
'''

'''
@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "unauthorized"
    }), 401
'''

# error handler for Auth
@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


# error handler for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400


# error handler for 405
@app.errorhandler(405)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": "method not allowed"
    }), 405


# error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "internal server error"
    }), 500
