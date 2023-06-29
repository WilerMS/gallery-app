from models.db import mongo
from bson.objectid import ObjectId
from utils.json import get_json_property


class ImagesService:
  @staticmethod
  def get_images(user=None):
    if user:
      return mongo.db.images.find({ 'user': user })
    else:
      return mongo.db.images.find()

  @staticmethod
  def get_images_by_label(image_label: str, user=None):
    dict = { 
      'label': {
        '$regex': f'.*{image_label}.*', 
        '$options': 'i' 
      }
    }

    if user:
      dict['user'] = user

    image = mongo.db.images.find(dict)
    return image

  @staticmethod
  def create_image(body):
    label = body['label']
    url = body['url']
    user = body['user']

    if not label or not url or not user:
      return False

    res = mongo.db.images.insert_one({
      'label': label, 
      'url': url, 
      'user': user,
      'likes': 0
    })

    return res.inserted_id

  @staticmethod
  def update_image(id, body):

    label = get_json_property(body, 'label')
    url = get_json_property(body, 'url')
    user = get_json_property(body, 'user')

    dict_to_update = { 'label': label, 'url': url }
    dict_to_update = {k: v for k, v in dict_to_update.items() if v is not None}

    res = mongo.db.images.update_one(
      { '_id': ObjectId(id), 'user': user },
      {'$set': dict_to_update}
    )

    return res.modified_count > 0 or (res.modified_count == 0 and res.matched_count > 0)

  @staticmethod
  def delete_image(image_id, user):
    res = mongo.db.images.delete_one({ '_id': ObjectId(image_id), 'user': user })
    return res.deleted_count > 0

  @staticmethod
  def like_image(id: str):
    res = mongo.db.images.update_one(
      { '_id': ObjectId(id) },
      {'$inc': {  'likes': 1 }}
    )
    return res.modified_count > 0

  @staticmethod
  def unlike_image(id: str):
    res = mongo.db.images.update_one(
      { '_id': ObjectId(id) },
      {'$inc': {  'likes': -1 }}
    )
    return res.modified_count > 0
