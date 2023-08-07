from typing import List
import copy

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

def replace_schema_require_properties(schema: dict, properties: List[str]):
  new_schema = copy.deepcopy(schema)
  new_schema['required'] = properties
  return new_schema

def delete_schema_properties(schema: dict, properties: List[str]):
  new_schema = copy.deepcopy(schema)
  for property in properties:
    if property in new_schema['required']:
      new_schema['required'].remove(property)
    del new_schema["properties"][property]
  return new_schema

