import graphene
import backend.views as views
from graphene import types


class WeatherInfo(graphene.ObjectType):
  temp = graphene.Float()
  humidity = graphene.Float()
  date = graphene.String()


class Query(graphene.ObjectType):
  hello = graphene.String(description='A typical hello world')
  weather = graphene.List(WeatherInfo, limit=graphene.Int())
  
  def resolve_hello(self, info):
    return 'World'
  
  def resolve_weather(self, info, limit: int):
    rv = views.get_weather_limited(limit)
    rv = list(map(lambda x: WeatherInfo(temp=x['temp'], humidity=x['humidity'], date=x['date']), rv))
    return rv


schema = graphene.Schema(query=Query)
