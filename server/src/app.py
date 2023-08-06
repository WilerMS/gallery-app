from flask import Flask
from flask_cors import CORS
from routes.users import users
from routes.auth import auth
from werkzeug.exceptions import HTTPException
import errors.error_handles as errors
from pymongo.errors import PyMongoError, DuplicateKeyError


app = Flask(__name__)

# CORS policy
# Allow those domains which can access the server
CORS(app)


# Import routes
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(auth, url_prefix='/auth')


# Registering errors
app.register_error_handler(400, errors.handle_validation_error)
app.register_error_handler(DuplicateKeyError, errors.handle_db_duplicate_key_error)
app.register_error_handler(PyMongoError, errors.handle_exception)
app.register_error_handler(HTTPException, errors.handle_exception)
