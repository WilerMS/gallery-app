from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.images import Images

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Images, '/images', '/images/<string:image_param>')