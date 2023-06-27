from models.db import mongo
from bson.objectid import ObjectId

class ImagesService:
  @staticmethod
  def get_all_images():
    images = mongo.db.images.find()
    return images

  @staticmethod
  def get_one_image(image_label: str):
    image = mongo.db.images.find_one({ 'label': image_label })
    return image

  @staticmethod
  def post_one_image(body):
    label = body['label']
    url = body['url']
    user = body['user']

    if not label or not url or not user:
      return False

    mongo.db.images.insert_one({ 
      'label': label, 
      'url': url, 
      'user': user 
    })

    return True

  @staticmethod
  def put_one_image(id, body):

    label = body['label']
    url = body['url']
    user = body['user']

    if not label or not url or not user:
      return False

    mongo.db.images.update_one(
      { '_id': ObjectId(id) },
      {'$set': { 'label': label, 'url': url, 'user': user }}
    )

    return True

  @staticmethod
  def delete_one_image(image_id):
    mongo.db.images.delete_one({ '_id': ObjectId(image_id) })
    return True
