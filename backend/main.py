from flask import jsonify
from backend import app
from backend.views import url_weather_data, url_student_info
from backend.ql import schema
from flask_graphql import GraphQLView

app.add_url_rule('/', 'home', lambda: jsonify({'response': 'ok', 'message': 'hey, patrick\'s data warehouse'}))
app.add_url_rule('/weather', 'post_weather', url_weather_data, methods=["GET", "POST"])
app.add_url_rule('/student', 'student', url_student_info)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
