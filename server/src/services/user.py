from models.db import mongo
from bson.objectid import ObjectId
from utils.json import get_json_property

class UsersService:

  @staticmethod
  def add_user(user):
    username = user['username']
    res = mongo.db.users.insert_one({
      'username': username,
      'liked_images': []
    })
    return res.inserted_id

  @staticmethod
  def add_like(user: str, image_id: str):
    res = mongo.db.users.update_one(
      { '_id': ObjectId(id), 'user': user },
      {'$push': { 'liked_images':  image_id  } }
    )
    return res.modified_count > 0 or (res.modified_count == 0 and res.matched_count > 0)

  @staticmethod
  def remove_like(user: str, image_id: str):
    res = mongo.db.users.update_one(
      { '_id': ObjectId(id), 'user': user },
      {'$pull': { 'liked_images':  image_id  } }
    )
    return res.modified_count > 0 or (res.modified_count == 0 and res.matched_count > 0)
