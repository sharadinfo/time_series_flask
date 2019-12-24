from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class helloworld(Resource):
	def get(self):
		return {'about': 'hello work with restful api'}
	def post(self):
		some_json = request.get_json()
		return {'you sent': some_json},201

class users(Resource):
	def get(self):
		return {'data': 'here is another one is route'}


api.add_resource(helloworld, '/')
api.add_resource(users, '/users')

if __name__ == '__main__':
	app.run(debug=True)

