from models.db import mongo
from bson.objectid import ObjectId
from utils.json import parse_cursor_to_json, get_json_property

collection = mongo.db['user']
class UsersService:
  
  @staticmethod
  def find_user(username: str):
    data_to_find = { 'username': username }
    return collection.find_one(data_to_find, { 'password': 0 })

  @staticmethod
  def create_user(user_data: dict):
    res = collection.insert_one({ **user_data, 'liked_images': [] })
    if not res.inserted_id:
      return None
    return collection.find_one({'_id': ObjectId(res.inserted_id)}, {'password': 0})

  @staticmethod
  def update_user(username, data: dict):
    res = collection.update_one({ 'username': username }, { '$set': data })
    if bool(res.modified_count > 0 or (res.modified_count == 0 and res.matched_count > 0)):
      return collection.find_one({ 'username': username })
    return None

  @staticmethod
  def get_likes(username: str):
    user = collection.find_one({ 'username': username })
    if user:
      user_dict = parse_cursor_to_json(user)
      liked_images = get_json_property(user_dict, 'liked_images')
      if liked_images:
        return liked_images
    return []

  @staticmethod
  def add_like(username: str, image_id: str):
    res = collection.update_one(
      { 'username': username },
      { '$push': { 'liked_images': image_id  } }
    )
    return bool(res.modified_count > 0 or (res.modified_count == 0 and res.matched_count > 0))

  @staticmethod
  def remove_like(username: str, image_id: str):
    res = collection.update_one(
      { 'username': username },
      { '$pull': { 'liked_images': image_id  } }
    )
    return bool(res.modified_count > 0 or (res.modified_count == 0 and res.matched_count > 0))
