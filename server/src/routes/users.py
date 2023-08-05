from flask import Blueprint, jsonify, request, Response
from bson import json_util
from models.Users import UsersModel
from flask_expects_json import expects_json
from schemas.users_schema import users_route_schema
from utils.schema_utils import replace_schema_require_properties
from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash, check_password_hash

users = Blueprint('users', __name__)

### GET ###
@users.route('/<string:username>', methods=['GET'])
def get_user(username: str):
  user = UsersModel.find_one(username)
  if not user:
    raise NotFound("User not found")
  return Response(json_util.dumps(user), mimetype='application/json')

### POST ###
@users.route('/', methods=['POST'])
@expects_json(users_route_schema)
def create_user():
  user_data = request.json

  # Password crypted to prevent security vulnerabilities
  user_data['password'] = generate_password_hash(user_data['password'])

  user = UsersModel.insert_one(user_data)
  return Response(json_util.dumps(user), mimetype='application/json')

### PUT ###
@users.route('/<string:id>', methods=['PUT'])
@expects_json(replace_schema_require_properties(users_route_schema, []))
def update_user(id: str):
  user = UsersModel.find_one_by_id(id)
  if not user:
    raise NotFound("User not found")
  user_data = request.json
  user = UsersModel.update_one(id, user_data)
  return Response(json_util.dumps(user), mimetype='application/json')

### DELETE ###
@users.route('/<string:id>', methods=['DELETE'])
def delete_user(id: str):
  user = UsersModel.find_one_by_id(id)
  if not user:
    raise NotFound("User not found")
  UsersModel.delete_one(id)
  return jsonify({ "message": "User Successfully deleted"}), 200