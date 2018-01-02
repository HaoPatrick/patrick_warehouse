import graphene
import backend.views as views


class WeatherInfo(graphene.ObjectType):
  temp = graphene.Float()
  humidity = graphene.Float()
  date = graphene.String(required=False)


class NewsInfo(graphene.ObjectType):
  id = graphene.Int()
  author = graphene.String()
  title = graphene.String()
  description = graphene.String()
  url = graphene.String()
  date = graphene.String()
  source = graphene.String()
  importance = graphene.Int()


class StudentInfo(graphene.ObjectType):
  student_id = graphene.String()
  name = graphene.String()
  grade = graphene.String()
  major = graphene.String()
  sex = graphene.String()
  class_name = graphene.String()
  social_id = graphene.String()


class Query(graphene.ObjectType):
  hello = graphene.String(description='A typical hello world')
  weather = graphene.List(WeatherInfo, limit=graphene.Int())
  student = graphene.Field(StudentInfo, student_id=graphene.String())
  news = graphene.List(NewsInfo, limit=graphene.Int())
  
  def resolve_hello(self, info):
    return 'World'
  
  def resolve_weather(self, info, limit: int):
    rv = views.get_weather_limited(limit)
    rv = list(map(lambda x: WeatherInfo(temp=x['temp'], humidity=x['humidity'], date=x['date']), rv))
    return rv
  
  def resolve_student(self, info, student_id: str):
    rv = views.get_student_info(student_id)
    rv = StudentInfo(student_id=rv[0], name=rv[1], grade=rv[2], major=rv[3], class_name=rv[4], sex=rv[5],
                     social_id=rv[6])
    return rv
  
  def resolve_news(self, info, limit: int):
    rv = views.get_news_limited(limit)
    print(rv)
    new_info_list = list(map(lambda x: NewsInfo(
      id=x[0], author=x[1], title=x[2], description=x[3],
      url=x[4], date=x[5], source=x[6], importance=x[7]
    ), rv))
    # print(new_info_list)
    return new_info_list


class AddWeather(graphene.Mutation):
  class Arguments:
    temp = graphene.Float()
    humidity = graphene.Float()
  
  ok = graphene.Boolean()
  weather = graphene.Field(lambda: WeatherInfo)
  
  def mutate(self, info, temp: float, humidity: float):
    views.add_weather(temp=temp, humidity=humidity)
    weather = WeatherInfo(temp=temp, humidity=humidity)
    ok = True
    return AddWeather(weather=weather, ok=ok)


class Mutation(graphene.ObjectType):
  add_weather = AddWeather.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
