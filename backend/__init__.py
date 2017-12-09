# from .main import app
from flask import Flask

app = Flask(__name__)
from .error_handler import InvalidParameter
from .views import get_weather_limited, add_weather
