from flask import Blueprint, jsonify, request, Response
from bson import json_util
from models.UsersModel import UsersModel
from flask_expects_json import expects_json
from schemas.users_schema import users_route_schema
from utils.schema_utils import replace_schema_require_properties
from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash
from middlewares.auth_middleware import auth_middleware

users = Blueprint('users', __name__)

### GET ###
@users.route('/<string:username>', endpoint='get_user', methods=['GET'])
@auth_middleware()
def get_user(username: str):
  user = UsersModel.find_one(username)
  if not user:
    raise NotFound("User not found")
  return Response(json_util.dumps(user), mimetype='application/json')

### POST ###
@users.route('/', endpoint='post_user', methods=['POST'])
@expects_json(users_route_schema)
def post_user():
  user_data = request.json

  # Password crypted to prevent security vulnerabilities
  user_data['password'] = generate_password_hash(user_data['password'])

  user = UsersModel.insert_one(user_data)
  return Response(json_util.dumps(user), mimetype='application/json')

### PUT ###
@users.route('/<string:id>', endpoint='put_user', methods=['PUT'])
@auth_middleware()
@expects_json(replace_schema_require_properties(users_route_schema, []))
def put_user(current_user, id: str):
  user = UsersModel.find_one_by_id(id)
  if not user:
    raise NotFound("User not found")
  user_data = request.json
  user = UsersModel.update_one(id, user_data)
  return Response(json_util.dumps(user), mimetype='application/json')

### DELETE ###
@users.route('/<string:id>', endpoint='delete_user', methods=['DELETE'])
@auth_middleware()
def delete_user(current_user, id: str):
  user = UsersModel.find_one_by_id(id)
  if not user:
    raise NotFound("User not found")
  UsersModel.delete_one(id)
  return jsonify({ "message": "User Successfully deleted"}), 200