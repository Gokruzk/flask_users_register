from flask import Flask, request, Response, jsonify
from flask_pymongo import PyMongo
from bson import json_util, ObjectId
from flask_cors import CORS, cross_origin

app = Flask(__name__)
database = 'orchestra'
app.config['MONGO_URI'] = f'mongodb://localhost:27017/{database}'
mongo = PyMongo(app)

CORS(app, resources={r"/user/*": {"origins": "http://localhost:3000"}})


@cross_origin
@app.route('/user', methods=['POST'])
def create_user():
    # receiving data
    username = request.json['username']

    email = request.json['email']
    # insert into mongo collection
    us = mongo.db.users.insert_one(
        {
            'username': username,
            'email': email
        }
    )
    response = {
        'id': str(us),
        'username': username,
        'email': email
    }
    return response


@cross_origin
@app.route('/user', methods=['GET'])
def get_users():
    # retreiving data
    us = mongo.db.users.find()
    response = json_util.dumps(us)
    return Response(response, mimetype='application/json')


@cross_origin
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    response = ''
    try:
        us = mongo.db.users.find_one({'_id': ObjectId(id)})
        response = json_util.dumps(us)
    except:
        print('An error has occurred while getting the user.')
    return response


@cross_origin
@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    response = ''
    try:
        mongo.db.users.delete_one({'_id': ObjectId(id)})
        response = jsonify({
            "message": "User deleted",
            "status": 200
        })
        response.status_code = 200
    except:
        print('An error has occurred while removing the user.')
    return response


@cross_origin
@app.route('/user/<id>', methods=['POST'])
def update_user(id):
    response = ''
    try:
        mongo.db.users.update_one({'_id': ObjectId(id)})
        response = jsonify({
            "message": "User deleted",
            "status": 200
        })
        response.status_code = 200
    except:
        print('An error has occurred while removing the user.')
    return response


if __name__ == "__main__":
    app.run(port=5001, debug=True)
