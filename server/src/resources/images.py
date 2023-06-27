from flask import request, Response
from flask_restful import Resource
from bson import json_util
from services.images import ImagesService

class ImagesController(Resource):
  def get(self, image_param=None):
    images = None
    if image_param:
      images = ImagesService.get_one_image(image_param)
    else:
      images = ImagesService.get_all_images()

    response = json_util.dumps(images)
    return Response(response, mimetype='application/json')

  def post(self):
    image = ImagesService.post_one_image(request.json)
    return 'Inserted' if image else 'Error'

  def put(self, image_param):
    image = ImagesService.put_one_image(image_param, request.json)
    return image

  def delete(self, image_param):
    response = ImagesService.delete_one_image(image_param)
    return response