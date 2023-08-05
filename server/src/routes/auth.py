from flask import Blueprint, jsonify, request, Response
from models.Users import UsersModel
from flask_expects_json import expects_json
from schemas.auth_schema import auth_login_route_schema, auth_register_route_schema
from werkzeug.exceptions import Unauthorized, BadRequest
from werkzeug.security import generate_password_hash, check_password_hash
from constants.env import JWT_SECRET_KEY
from utils.json import parse_cursor_to_json
import jwt
from routes.users import create_user

auth = Blueprint('auth', __name__)

### POST LOGIN ###
@auth.route('/login', methods=['POST'])
@expects_json(auth_login_route_schema)
def login():
  username = request.json['username']
  password = request.json['password']

  user = UsersModel.find_one(username, True)

  if not user:
    raise Unauthorized("Invalid credentials")
  
  valid_user = check_password_hash(user['password'], password)

  if not valid_user:
    raise Unauthorized("Invalid credentials")
  
  user = UsersModel.find_one(username)
  user['_id'] = str(user['_id'])

  token = jwt.encode(
    user,
    JWT_SECRET_KEY,
    algorithm="HS256"
  )
  
  return token

### POST REGISTER ###
@auth.route('/register', methods=['POST'])
@expects_json(auth_register_route_schema)
def register():
  user_data = request.json

  # Comparing passwords
  password = user_data['password']
  confirm_password = user_data['confirmPassword']
  if password != confirm_password:
    raise BadRequest("Passwords must match")
  
  del user_data['confirmPassword']

  # Password crypted to prevent security vulnerabilities
  user_data['password'] = generate_password_hash(user_data['password'])

  # Creating user in database
  user = UsersModel.insert_one(user_data)
  user['_id'] = str(user['_id'])

  token = jwt.encode(
    user,
    JWT_SECRET_KEY,
    algorithm="HS256"
  )

  return token