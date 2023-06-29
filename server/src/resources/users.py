from flask import request, Response, jsonify
from flask_restful import Resource, abort
from bson import json_util
from services.users import UsersService
from utils.json import get_json_property, parse_cursor_to_json

class UsersController(Resource):

  ### [get] method
  def get(self, username):

    if not username:
      abort(400, message="Invalid username", error=True)

    user = UsersService.get_user(username)

    if not user:
      abort(400, message="Invalid username", error=True)

    user_to_send = parse_cursor_to_json(user)

    return  Response(json_util.dumps(user_to_send), mimetype='application/json')

  ### [POST] method
  def post(self):

    username = get_json_property(request.json, 'username')

    if not username:
      abort(400, message="Invalid username", error=True)

    inserted = UsersService.add_user(username)

    if not inserted:
      abort(400, message="Invalid username", error=True)

    return jsonify({ 'error': False, 'message': 'Success' })