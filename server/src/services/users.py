from models.db import mongo
from bson.objectid import ObjectId

class UsersService:

  @staticmethod
  def get_user(username):
    return mongo.db.users.find_one({
      'username': username
    })

  @staticmethod
  def create_user(username):
    res = mongo.db.users.insert_one({
      'username': username,
      'liked_images': []
    })
    return res.inserted_id

  @staticmethod
  def update_user(username, data: dict):
    res = mongo.db.users.update_one(
      { 'username': username },
      data
    )
    return res

  @staticmethod
  def get_likes(user: str):
    res = mongo.db.users.find_one(
      { 'username': user },
      { 'liked_images': 1 }
    )
    return res

  @staticmethod
  def add_like(user: str, image_id: str):
    res = mongo.db.users.update_one(
      { 'username': user },
      { '$push': { 'liked_images': image_id  } }
    )
    return res.modified_count > 0 or (res.modified_count == 0 and res.matched_count > 0)

  @staticmethod
  def remove_like(user: str, image_id: str):
    res = mongo.db.users.update_one(
      { 'username': user },
      { '$pull': { 'liked_images': image_id  } }
    )
    return res.modified_count > 0 or (res.modified_count == 0 and res.matched_count > 0)
