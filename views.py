from connection import WeatherDB


def add_weather(temp: float, humidity: float):
  weather_db = WeatherDB()
  weather_db.insert_data(temp, humidity)
