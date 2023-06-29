from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.images import ImagesController
from resources.users import UsersController

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(
  ImagesController,
  '/images',
  '/images/<string:param>',
  '/images/<string:param>/<string:action>'
)

api.add_resource(UsersController, '/users', '/users/<string:username>')