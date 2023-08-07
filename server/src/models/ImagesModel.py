from .db import db
from schemas.images_schema import images_db_schema
from flask_pymongo.wrappers import Collection
from flask_pymongo import ObjectId

IMAGES_MODEL = "images"

if IMAGES_MODEL not in db.list_collection_names():
  db.create_collection(IMAGES_MODEL, validator=images_db_schema)

collection: Collection = db[IMAGES_MODEL]

class ImagesModel:

  @staticmethod
  def find_many(query: dict, page: int = 1, limit: int = 10):
    skip = (page - 1) * limit
    images = list(collection.find(query).skip(skip).limit(limit))
    return images

  @staticmethod
  def find_one(id: str):
    query = { '_id': ObjectId(id) }
    image = collection.find_one(query)
    return image

  @staticmethod
  def insert_one(image: dict):
    r = collection.insert_one({ **image, 'likes': 0 })
    image = collection.find_one(
      { '_id': ObjectId(r.inserted_id) },
      { 'password': 0 }
    )
    return image
  
  @staticmethod
  def update_one(id: str, data: dict):
    query = { '_id': ObjectId(id) }
    collection.update_one(query, { '$set': data })
    image = collection.find_one(query)
    return image
  
  @staticmethod
  def delete_one(id: str):
    query = { '_id': ObjectId(id) }
    collection.delete_one(query)
    return True 