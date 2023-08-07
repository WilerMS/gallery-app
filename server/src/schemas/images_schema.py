import utils.schema_utils as schema_utils

images_route_schema = {
  "type": "object",
  "additionalProperties": False,
  "required": ["title", "url", "userId"],
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

images_post_route_schema = schema_utils.delete_schema_properties(images_route_schema, ['likes', 'userId'])
images_put_route_schema = schema_utils.replace_schema_require_properties(images_post_route_schema, [])
images_db_schema = {
  "$jsonSchema": schema_utils.transform_schema_to_mongo_schema(images_route_schema)
}
