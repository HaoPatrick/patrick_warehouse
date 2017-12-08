from flask import Flask, request, jsonify
import views

app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hello World!'


@app.route('/weather', methods=['POST'])
def post_weather_data():
  if request.method == 'POST':
    try:
      views.add_weather(request.form['temp'], request.form['humidity'])
    except Exception as e:
      return e
    return jsonify({
      'status': 200, 'response': 'OK'
    })


if __name__ == '__main__':
  app.run()
