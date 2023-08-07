from flask import Blueprint, request

images = Blueprint('images', __name__)

### GET ONE IMAGE ###
@images.route('/<string:id>', endpoint='get_image', methods=['GET'])
def get_image(id: str):
  return id


### GET IMAGES ###
@images.route('/', endpoint='get_images', methods=['GET'])
def get_images():
  args = request.args
  return args


### POST IMAGE ###
@images.route('/', endpoint='post_image', methods=['POST'])
def post_image():
  body = request.json
  return body


### UPDATE IMAGE ###
@images.route('/<string:id>', endpoint='put_image', methods=['PUT'])
def put_image(id: str):
  body = request.json
  return {
    "id": id,
    "body": body
  }


### DELETE IMAGE ###
@images.route('/<string:id>', endpoint='delete_image', methods=['DELETE'])
def delete_image(id: str):
  return {
    "id": id
  }