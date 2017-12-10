from flask import request, jsonify
from backend import views, error_handler
from backend import app


# app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'


@app.route('/weather', methods=['POST', 'GET'])
def post_weather_data():
  if request.method == 'POST':
    try:
      views.add_weather(request.form['temp'], request.form['humidity'])
    except Exception as e:
      return e
    return jsonify({
      'response': 'ok'
    })
  elif request.method == 'GET':
    try:
      weather = views.get_weather_limited(request.args['limit'])
    except KeyError:
      raise error_handler.InvalidParameter("invalid parameter")
    return jsonify({
      'response': 'ok',
      'weather': weather
    })


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
