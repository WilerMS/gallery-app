from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.images import ImagesController

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(ImagesController, '/images', '/images/<string:image_param>')