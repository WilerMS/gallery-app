auth_login_route_schema = {
  "type": "object",
  "additionalProperties": False,
  "required": ["username", "password"],
  "properties": {
    "username": {
      "type": "string"
    },
    "password": {
      "type": "string"
    }
  }
}

auth_register_route_schema = {
  "type": "object",
  "additionalProperties": False,
  "required": ["username", "name", "password", "confirmPassword"],
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
    "confirmPassword": {
      "type": "string"
    }
  }
}