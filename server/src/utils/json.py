def get_json_property(json, key):
  try:
    return json[key]
  except KeyError:
    return None