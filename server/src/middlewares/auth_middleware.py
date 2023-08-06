from typing import Callable
from flask import request
from werkzeug.exceptions import Unauthorized, BadRequest
from constants.env import JWT_SECRET_KEY
from models.UsersModel import UsersModel
import jwt

def auth_middleware(function: Callable):
  def decorated(*args, **kwargs):
    token = None
    if "Authorization" in request.headers:
      token = request.headers["Authorization"].split(" ")[1]

    if not token:
      raise Unauthorized("Provided token is not valid")
    
    data = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
    username = data['username']

    user = UsersModel.find_one(username)

    if not user:
      raise Unauthorized("Provided token is not valid")
    
    current_user = user
    return function(current_user, *args, **kwargs)
  
  return decorated