from flask import request, Response, jsonify
from flask_restful import Resource, abort
from bson import json_util
from services.images import ImagesService
from services.users import UsersService
from utils.json import get_json_property, parse_cursor_to_json
from utils.validation import validate_body, validate_partial_body

class ImagesController(Resource):
	### [GET] method
	def get(self, param=None):
		images = None
		user = get_json_property(request.args, "user")

		if param:
			images = ImagesService.find_images_by_label(param, user)
		else:
			images = ImagesService.find_images(user)

		response = parse_cursor_to_json(images)

		### matching user like with images
		likes = UsersService.get_likes(user)
		liked_images = parse_cursor_to_json(likes)

		if liked_images:
			for image in response:
				image["is_liked"] = str(image["_id"]) in liked_images["liked_images"]

		return Response(json_util.dumps(response), mimetype="application/json")

    ### [POST] method
	def post(self, param=None, action=None):

		### INSERT LIKES
		if param and action == "like":
            
			keys = ["username"]
			user = validate_body(request.json, keys)
			username = user['username']

			inserted = ImagesService.like_image(param)

			if not inserted:
				abort(500, message="Something went wrong", error=True)

            ### Add image to likes in UserService
			liked = UsersService.add_like(username, param)

			if not liked:
				abort(500, message="Something went wrong", error=True)

			return jsonify({"error": False, "message": "Success"})

		### DELETE LIKES
		elif param and action == "unlike":

			keys = ["username"]
			user = validate_body(request.json, keys)
			username = user['username']

			inserted = ImagesService.unlike_image(param)

			if not inserted:
				abort(400, message="Something went wrong", error=True)

			### Delete image to likes in UserService
			unliked = UsersService.remove_like(username, param)

			if not unliked:
				abort(400, message="Something went wrong", error=True)

			return jsonify({"error": False, "message": "Success"})

		### INSERT IMAGE
		keys = ['label', 'description', 'url', 'private', 'tags', 'username']
		image_data = validate_body(request.json, keys)

		image = ImagesService.create_image(image_data)

		if not image:
			abort(400, message="Something went wrong", error=True)

		return jsonify({"error": False, "message": "Success"})

    ### [PUT] method
	def put(self, param):
		keys = ['label', 'description', 'url', 'private', 'tags', 'username']
		image_data = validate_partial_body(request.json, keys)

		if not image_data['username']:
			abort(400, message="Invalid user id", error=True)

		image = ImagesService.update_image(param, image_data)

		if not image:
			abort(400, message="Something went wrong", error=True)

		return jsonify({"error": False, "message": "Success"})

    ### [DELETE] method
	def delete(self, param):

		keys = ["username"]
		user = validate_body(request.json, keys)
		username = user['username']

		res = ImagesService.delete_image(param, username)

		if not res:
			abort(404, message="Something went wrong", error=True)

		return jsonify({"message": "Success", "error": False})
