from flask import jsonify
from backend import app
from backend.views import post_weather_data

app.add_url_rule('/', 'home', lambda: jsonify({'response': 'ok', 'message': 'hey, patrick\'s data warehouse'}))
app.add_url_rule('/weather', 'post_weather', post_weather_data)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
