from bson import json_util

def get_json_property(json, key):
  try:
    return json[key]
  except KeyError:
    return None

def parse_cursor_to_json(obj):
  response_str = json_util.dumps(obj)
  response_json = json_util.loads(response_str)
  return response_json