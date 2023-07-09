from flask import request, Response, jsonify
from flask_restful import Resource, abort
from bson import json_util
from services.users import UsersService
from utils.json import parse_cursor_to_json
from utils.validation import validate_body

class UsersController(Resource):

  ### [get] method
  def get(self, username=None):

    if not username:
      abort(400, message="Invalid username", error=True)

    user = UsersService.find_user(username)

    if not user:
      abort(404, message="User not found", error=True)

    user_to_send = parse_cursor_to_json(user)

    return  Response(json_util.dumps(user_to_send), mimetype='application/json')

  ### [POST] method
  def post(self):

    keys = ['username', 'name', 'avatarUrl', 'password']
    user_data = validate_body(request.json, keys)

    user = UsersService.create_user(user_data)

    if not user:
      abort(500, message="Internal server Error", error=True)

    return jsonify({ 'error': False, 'message': 'Success' })