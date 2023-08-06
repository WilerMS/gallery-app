from utils.schema_utils import transform_schema_to_mongo_schema

images_route_schema = {
  "type": "object",
  "additionalProperties": False,
  "required": ["title", "url", "likes", "userId"],
  "properties": {
    "title": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "url": {
      "type": "string"
    },
    "private": {
      "type": "boolean",
      "default": False
    },
    "likes": {
      "type": "number",
      "default": 0
    },
    "userId": {
      "type": "string"
    }
  }
}

images_db_schema = {
  "$jsonSchema": transform_schema_to_mongo_schema(images_route_schema)
}