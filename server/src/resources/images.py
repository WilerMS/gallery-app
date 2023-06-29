from flask import request, Response, jsonify
from flask_restful import Resource, abort
from bson import json_util
from services.images import ImagesService
from services.users import UsersService
from utils.json import get_json_property, parse_cursor_to_json

class ImagesController(Resource):

  ### [GET] method
  def get(self, param=None):

    images = None
    user = get_json_property(request.args, 'user')
    
    if param:
      images = ImagesService.get_images_by_label(param, user)
    else:
      images = ImagesService.get_images(user)

    response = parse_cursor_to_json(images)

    ### matching user like with images
    likes = UsersService.get_likes(user)
    liked_images = parse_cursor_to_json(likes)

    print ('liked_images')
    print (liked_images['liked_images'])
    print (liked_images['liked_images'])

    for image in response:
      image['is_liked'] = str(image['_id']) in liked_images['liked_images']

    return Response(json_util.dumps(response), mimetype='application/json')

  ### [POST] method
  def post(self, param=None, action=None):

    user = get_json_property(request.json, 'user')

    if not user:
      abort(400, message="Invalid user id")

    if param and action == 'like':
      inserted = ImagesService.like_image(param)

      if not inserted:
        abort(400, message="Something went wrong", error=True)
      
      ### Add image to likes in UserService
      liked = UsersService.add_like(user, param)

      if not liked:
        abort(400, message="Something went wrong", error=True)

      return jsonify({ 'error': False, 'message': 'Success' })

    elif param and action == 'unlike':
      inserted = ImagesService.unlike_image(param)

      if not inserted:
        abort(400, message="Something went wrong", error=True)
      
      ### Delete image to likes in UserService
      unliked = UsersService.remove_like(user, param)

      if not unliked:
        abort(400, message="Something went wrong", error=True)

      return jsonify({ 'error': False, 'message': 'Success' })

    else:
      inserted_id = ImagesService.create_image(request.json)

      if not inserted_id:
        abort(400, message="Something went wrong", error=True)

    return jsonify({ 'error': False, 'message': 'Success' })

  ### [PUT] method
  def put(self, param):
    user = get_json_property(request.json, 'user')

    if not user:
      abort(400, message="Invalid user id", error=True)
    
    upserted = ImagesService.update_image(param, request.json)

    if not upserted:
        abort(400, message="Something went wrong", error=True)

    return jsonify({ 'error': False, 'message': 'Success' })

  ### [DELETE] method
  def delete(self, param):

    user = get_json_property(request.json, 'user')

    if not user:
      abort(400, message="Invalid user id", error=True)

    res = ImagesService.delete_image(param, user)

    if not res:
      abort(404, message="Something went wrong", error=True)

    return jsonify({ 'message': 'Success', 'error': False })