from utils.schema_utils import transform_schema_to_mongo_schema

users_route_schema = {
  "type": "object",
  "additionalProperties": False,
  "required": ["username", "name", "password"],
  "properties": {
    "username": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "avatar": {
      "type": "string"
    },
    "password": {
      "type": "string"
    },
    "likedImages": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}

users_db_schema = {
  "$jsonSchema": transform_schema_to_mongo_schema(users_route_schema)
}