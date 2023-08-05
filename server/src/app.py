from flask import Flask
from flask_cors import CORS
from routes.users import users
from werkzeug.exceptions import HTTPException
from flask_expects_json import ValidationError
from errors.errors import handle_exception, handle_validation_error, handle_db_duplicate_key_error
from pymongo.errors import PyMongoError, DuplicateKeyError

app = Flask(__name__)
CORS(app)

app.register_blueprint(users, url_prefix='/users')

# Registering errors
app.register_error_handler(400, handle_validation_error)
app.register_error_handler(DuplicateKeyError, handle_db_duplicate_key_error)
app.register_error_handler(PyMongoError, handle_exception)
app.register_error_handler(HTTPException, handle_exception)
