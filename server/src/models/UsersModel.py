from .db import db
from schemas.users_schema import users_db_schema
from flask_pymongo.wrappers import Collection
from flask_pymongo import ObjectId, ASCENDING

USER_MODEL = "users"

if USER_MODEL not in db.list_collection_names():
  db.create_collection(USER_MODEL, validator=users_db_schema)
  db[USER_MODEL].create_index([("username", ASCENDING)], unique=True)

collection: Collection = db[USER_MODEL]

class UsersModel:

  @staticmethod
  def find_one(username: str, include_password: bool = False):
    query = { 'username': username }
    user = collection.find_one(query, { 'password': 1 if include_password else 0 })
    return user
  
  @staticmethod
  def find_one_by_id(id: str):
    query = { '_id': ObjectId(id) }
    user = collection.find_one(query, { 'password': 0 })
    return user

  @staticmethod
  def insert_one(user: dict):
    r = collection.insert_one({ **user, 'likedImages': [] })
    user_data = collection.find_one(
      { '_id': ObjectId(r.inserted_id) },
      { 'password': 0 }
    )
    return user_data
  
  @staticmethod
  def update_one(id: str, data: dict):
    query = { '_id': ObjectId(id) }
    r = collection.update_one(query, { '$set': data })
    user = collection.find_one(query, { 'password': 0 })
    return user 
  
  @staticmethod
  def delete_one(id: str):
    query = { '_id': ObjectId(id) }
    collection.delete_one(query, { 'password': 0 })
    return True 