from flask import Blueprint, request, Response, jsonify
from flask_expects_json import expects_json
from bson import json_util
import schemas.images_schema as images_schemas
from models.ImagesModel import ImagesModel
from models.UsersModel import UsersModel
from werkzeug.exceptions import NotFound, BadRequest
from middlewares.auth_middleware import auth_middleware

images = Blueprint('images', __name__)

### GET ONE IMAGE ###
@images.route('/<string:id>', endpoint='get_image', methods=['GET'])
@auth_middleware(allow_unauthenticated=True)
def get_image(current_user, id: str):
  image = ImagesModel.find_one(id)

  # Check if current user owns a private image
  if image['private']:
    if not current_user:
      raise NotFound('Image Not found')
    elif str(current_user['_id']) != image['userId']:
      raise NotFound('Image Not found')

  image['isOwner'] = image['userId'] == str(current_user['_id'])
  image['liked'] = str(image['_id']) in current_user['likedImages']

  return Response(json_util.dumps(image), mimetype='application/json')


### GET IMAGES ###
@images.route('/', endpoint='get_images', methods=['GET'])
@auth_middleware(allow_unauthenticated=True)
def get_images(current_user):
  query = {}

  # Include tilte query param
  q = request.args.get('q', None)
  if q: 
    query['title'] = { '$regex': f'.*{q}.*', '$options': 'i' }

  # Finding userId
  owner_username = request.args.get('owner', None)
  owner = UsersModel.find_one(owner_username) if owner_username else None
  if owner:
    # Include userId query param
    query['userId'] = str(owner['_id'])

  # Include page and limit params  
  page = int(request.args.get('page', 1))
  limit = int(request.args.get('limit', 10))

  # Include logic for private photos
  if current_user:
    query['$or'] = [
      { "private": True, "userId": str(current_user['_id']) },
      { "private": False }
    ]
  else:
    query['private'] = False

  # Finding images
  images = ImagesModel.find_many(query, page, limit)

  for image in images:
    image['isOwner'] = bool(current_user) and image['userId'] == str(current_user['_id'])
    image['liked'] = bool(current_user) and str(image['_id']) in current_user['likedImages']
  
  return Response(json_util.dumps(images), mimetype='application/json')


### POST IMAGE ###
@images.route('/', endpoint='post_image', methods=['POST'])
@auth_middleware(allow_unauthenticated=False)
@expects_json(images_schemas.images_post_route_schema)
def post_image(current_user):
  body = request.json
  body['private'] = body.get('private', False)
  body['userId'] = str(current_user['_id'])
  image = ImagesModel.insert_one(body)
  image['_id']: str(image['_id'])
  return Response(json_util.dumps(image), mimetype='application/json')


### UPDATE IMAGE ###
@images.route('/<string:id>', endpoint='put_image', methods=['PUT'])
@auth_middleware(allow_unauthenticated=False)
@expects_json(images_schemas.images_put_route_schema)
def put_image(current_user, id: str):
  image = ImagesModel.find_one(id)

  # Check if the image already exists
  if not image:
    raise NotFound("Image not found")
  
  # Check if current user owns the current image
  if str(current_user['_id']) != image['userId']:
    raise BadRequest("You do not own this photo")
  
  # Update image
  image = ImagesModel.update_one(id, request.json)
  
  return Response(json_util.dumps(image), mimetype='application/json')


### DELETE IMAGE ###
@images.route('/<string:id>', endpoint='delete_image', methods=['DELETE'])
@auth_middleware(allow_unauthenticated=False)
def delete_image(current_user, id: str):
  image = ImagesModel.find_one(id)

  # Check if the image already exists
  if not image:
    raise NotFound("Image not found")
  
  # Check if current user owns the current image
  if str(current_user['_id']) != image['userId']:
    raise BadRequest("You do not own this image")

  # Delete Image
  ImagesModel.delete_one(id)

  return jsonify({ "message": "Image Successfully deleted" }), 200

### LIKE IMAGE ###
@images.route('/<string:id>/like', endpoint='like_image', methods=['POST'])
@auth_middleware(allow_unauthenticated=False)
def like_image(current_user, id: str):
  image = ImagesModel.find_one(id)

  # Check if the image already exists
  if not image:
    raise NotFound("Image not found")

  # Check if user liked the image before
  if str(image['_id']) in current_user['likedImages']:
    jsonify({ "message": "Like Successfully added" }), 200

  # Add like to image
  ImagesModel.like(id)

  # Add like to user
  UsersModel.like_image(str(current_user['_id']), str(image['_id']))

  return jsonify({ "message": "Like Successfully added" }), 200

### UNLIKE IMAGE ###
@images.route('/<string:id>/unlike', endpoint='unlike_image', methods=['POST'])
@auth_middleware(allow_unauthenticated=False)
def unlike_image(current_user, id: str):
  image = ImagesModel.find_one(id)

  # Check if the image already exists
  if not image:
    raise NotFound("Image not found")
  
  # Check if user liked the image before
  if str(image['_id']) not in current_user['likedImages']:
    jsonify({ "message": "Like Successfully deleted" }), 200

  # Add like to image
  ImagesModel.unlike(id)
  
  # Add like to user
  UsersModel.unlike_image(str(current_user['_id']), str(image['_id']))

  return jsonify({ "message": "Like Successfully deleted" }), 200