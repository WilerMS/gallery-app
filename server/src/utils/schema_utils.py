def transform_schema_to_mongo_schema(schema: dict):
  new_schema = {}
  for key, value in schema.items():
    if key == 'type':
      new_schema['bsonType'] = value
    elif key == 'additionalProperties':
      continue
    elif key == 'properties':
      for j in schema['properties']:
        new_schema['properties'] = {}
        new_schema['properties'][j] = transform_schema_to_mongo_schema(schema['properties'][j])
    elif key == 'items':
      new_schema['items'] = transform_schema_to_mongo_schema(schema["items"])
    else:
      new_schema[key] = value

  return new_schema

def replace_schema_require_properties(schema: dict, properties: list):
  new_schema = schema.copy()
  new_schema['required'] = properties
  return new_schema
