from werkzeug.exceptions import HTTPException
from pymongo.errors import PyMongoError, DuplicateKeyError
from flask import json, jsonify

def handle_validation_error(e):
  error_message = str(e).split('\n', 1)[0].replace("400 Bad Request: ", '')
  response = jsonify({
      "code": 400,
      "name": "Bad Request",
      "description": error_message, #first line of error
  })
  return response, 400

def handle_db_duplicate_key_error(e: DuplicateKeyError):
  duplicated_data = e.details['keyValue']
  duplicated_key = list(duplicated_data.keys())[0]
  response = jsonify({
    "code": 400,
    "name": "Bad Request",
    "description": f'{duplicated_key} {duplicated_data[duplicated_key]} already exists', #first line of error
  })
  return response, 500

# Normalize all errors in a json
def handle_exception(e: HTTPException):
  # pass through HTTP errors
  response = e.get_response()
  response.data = json.dumps({
      "code": e.code,
      "name": e.name,
      "description": e.description,
  })
  response.content_type = "application/json"
  return response