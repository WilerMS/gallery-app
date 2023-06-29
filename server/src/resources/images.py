from flask import request, Response, jsonify
from flask_restful import Resource, abort
from bson import json_util
from services.images import ImagesService
from utils.json import get_json_property

class ImagesController(Resource):

  ### [GET] method
  def get(self, param=None):

    images = None
    user = get_json_property(request.json, 'user')
    
    if param:
      images = ImagesService.get_images_by_label(param, user)
    else:
      images = ImagesService.get_images(user)

    response = json_util.dumps(images)

    return Response(response, mimetype='application/json')

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

    elif param and action == 'unlike':
      inserted = ImagesService.unlike_image(param)

      if not inserted:
        abort(400, message="Something went wrong", error=True)
      
      ### Delete image to likes in UserService

    else:
      inserted_id = ImagesService.create_image(request.json)

      if not inserted_id:
        abort(400, message="Something went wrong", error=True)

    return jsonify({ 'error': False, 'message': 'Success' })

  ### [PUT] method
  def put(self, param):
    user = get_json_property(request.json, 'user')

    if not user:
      abort(400, message="Invalid user id")
    
    upserted = ImagesService.update_image(param, request.json)

    if not upserted:
        abort(400, message="Something went wrong", error=True)

    return jsonify({ 'error': False, 'message': 'Success' })

  ### [DELETE] method
  def delete(self, param):

    user = get_json_property(request.json, 'user')

    if not user:
      abort(400, message="Invalid user id")

    res = ImagesService.delete_image(param, user)

    if not res:
      abort(404, message="Something went wrong", error=True)

    return jsonify({ 'message': 'Success', 'error': False })