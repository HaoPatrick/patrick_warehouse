from flask import request, jsonify
from backend.db_connection import WeatherDB
from backend.error_handler import InvalidParameter


def add_weather(temp: float, humidity: float):
  weather_db = WeatherDB()
  weather_db.insert_data(temp, humidity)


def get_weather_limited(limit_to: int) -> list:
  weather_db = WeatherDB()
  rv = weather_db.get_data_limited(limit_to)
  rv = map(lambda x: {'humidity': x[1], 'temp': x[2], 'date': str(x[3])}, rv)
  return list(rv)


def post_weather_data():
  if request.method == 'POST':
    try:
      add_weather(request.form['temp'], request.form['humidity'])
    except Exception as e:
      return e
    return jsonify({
      'response': 'ok'
    })
  elif request.method == 'GET':
    try:
      weather = get_weather_limited(request.args['limit'])
    except KeyError:
      raise InvalidParameter("invalid parameter")
    return jsonify({
      'response': 'ok',
      'weather': weather
    })
