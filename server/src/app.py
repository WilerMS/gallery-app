from flask import Flask
from flask_cors import CORS
from routes.users import users
from routes.auth import auth
from werkzeug.exceptions import HTTPException
from errors.errors import handle_exception, handle_validation_error, handle_db_duplicate_key_error
from pymongo.errors import PyMongoError, DuplicateKeyError
import os


app = Flask(__name__)
CORS(app)


# Import routes
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(auth, url_prefix='/auth')


# Registering errors
app.register_error_handler(400, handle_validation_error)
app.register_error_handler(DuplicateKeyError, handle_db_duplicate_key_error)
app.register_error_handler(PyMongoError, handle_exception)
app.register_error_handler(HTTPException, handle_exception)
