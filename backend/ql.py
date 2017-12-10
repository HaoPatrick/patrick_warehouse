import graphene
import backend.views as views


class WeatherInfo(graphene.ObjectType):
  temp = graphene.Float()
  humidity = graphene.Float()
  date = graphene.String()


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


schema = graphene.Schema(query=Query)
