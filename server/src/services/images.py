from models.db import mongo
from bson.objectid import ObjectId
from utils.json import get_json_property

collection = mongo.db['images']

class ImagesService:
  @staticmethod
  def find_images(username: str = None):
    if username:
      return collection.find({ 'username': username })
    else:
      return collection.find({}, {})

  @staticmethod
  def find_images_by_label(label: str, user: str = None):
    dict = {
      'label': {
        '$regex': f'.*{label}.*', 
        '$options': 'i' 
      }
    }

    if user: dict['user'] = user

    return collection.find(dict)

  @staticmethod
  def create_image(image_data: dict):
    res = collection.insert_one({
      **image_data,
      'likes': 0
    })
    return collection.find_one({'_id': ObjectId(res.inserted_id)})

  @staticmethod
  def update_image(id: str, image_data: dict):
    query = {'_id': ObjectId(id)}
    res = collection.update_one(query, {'$set': image_data})
    if bool(res.modified_count > 0 or (res.modified_count == 0 and res.matched_count > 0)):
      return collection.find_one(query)
    return None

  @staticmethod
  def delete_image(image_id, username):
    res = collection.delete_one({ '_id': ObjectId(image_id), 'username': username})
    return res.deleted_count > 0

  @staticmethod
  def like_image(id: str):
    query = {'_id': ObjectId(id)}
    new_values = {'$inc': { 'likes': -1}}
    res = collection.update_one(query, new_values)
    return res.modified_count > 0

  @staticmethod
  def unlike_image(id: str):
    query = {'_id': ObjectId(id)}
    new_values = {'$inc': { 'likes': -1}}
    res = collection.update_one(query, new_values)
    return res.modified_count > 0
