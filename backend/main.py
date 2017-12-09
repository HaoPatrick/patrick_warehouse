from flask import Flask, request, jsonify
# from backend import error_handler, views
import backend

app = backend.app


@app.route('/')
def hello_world():
  return 'Hello World!'


@app.route('/weather', methods=['POST', 'GET'])
def post_weather_data():
  if request.method == 'POST':
    try:
      backend.views.add_weather(request.form['temp'], request.form['humidity'])
    except Exception as e:
      return e
    return jsonify({
      'response': 'ok'
    })
  elif request.method == 'GET':
    try:
      weather = backend.views.get_weather_limited(request.args['limit'])
    except KeyError:
      raise backend.error_handler.InvalidParameter("invalid parameter")
    return jsonify({
      'response': 'ok',
      'weather': weather
    })


if __name__ == '__main__':
  app.run()
