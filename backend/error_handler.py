from flask import jsonify
from backend import app


class InvalidParameter(Exception):
  status_code = 400
  
  def __init__(self, message: str, status_code=None, payload=None):
    Exception.__init__(self)
    self.message = message
    if status_code:
      self.status_code = status_code
    self.payload = payload
  
  def to_dict(self) -> dict:
    rv = dict(self.payload or ())
    rv['message'] = self.message
    rv['response'] = 'error'
    return rv


@app.errorhandler(InvalidParameter)
def handle_invalid_parameter(error: InvalidParameter):
  response = jsonify(error.to_dict())
  response.status_code = error.status_code
  return response
