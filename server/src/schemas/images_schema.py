images_schema = {
  "$jsonSchema": {
    "bsonType": "object",
    "additionalProperties": False,
    "required": ["title", "url", "likes", "userId"],
    "properties": {
      "title": {
        "bsonType": "string"
      },
      "description": {
        "bsonType": "string"
      },
      "url": {
        "bsonType": "string"
      },
      "private": {
        "bsonType": "boolean",
        "default": False
      },
      "likes": {
        "bsonType": "number",
        "default": 0
      },
      "userId": {
        "bsonType": "string"
      }
    }
  }
}