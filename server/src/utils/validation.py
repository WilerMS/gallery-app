from utils.json import get_json_property
from flask_restful import abort

def validate_body(body: dict, keys):
	dict = {}
	for key in keys:
		value = get_json_property(body, key)
		if value:
			dict[key] = value
		else:
			abort(400, message=f"Missing data, ({key})", error=True)
	
	print('dict')
	print(dict)
	return dict

def validate_partial_body(body: dict, keys):
	dict = {}
	for key in keys:
		value = get_json_property(body, key)
		if value:
			dict[key] = value
		
	for key, value in body:
		if key not in body:
			abort(400, message=f"Unexpected provided data, ({key})", error=True)
	
	return dict