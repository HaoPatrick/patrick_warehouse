from .db_connection import WeatherDB


def add_weather(temp: float, humidity: float):
  weather_db = WeatherDB()
  weather_db.insert_data(temp, humidity)


def get_weather_limited(limit_to: int) -> list:
  weather_db = WeatherDB()
  rv = weather_db.get_data_limited(limit_to)
  rv = map(lambda x: {'humidity': x[1], 'temp': x[2], 'date': x[3]}, rv)
  return list(rv)
