from flask import Flask, render_template, make_response
import jwt
import datetime
from flask import Flask, jsonify, request, url_for
import csv
from functools import wraps

import pickle
app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisthesecretkey'

def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = request.args.get('token')

		if not token:
			return jsonify({'message' : 'token is missing!'}), 403
		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])

		except:
			return jsonify({'message' : 'token is missing or invalid'}), 403

		return f(*args, **kwargs)
	return decorated

@app.route('/login')
def login():
	auth = request.authorization

	if auth and auth.password == 'password':
		token = jwt.encode({'user' : auth.username, 'password' : auth.password, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=15)}, app.config['SECRET_KEY'])

		return jsonify({'token' : token.decode('UTF-8')})

	return make_response('could not verify!' , 401, {'WWW-Authenticate' : 'Basic realm="login Required"'})
@app.route('/')
@token_required

#	users = ['sharad','suraj']
def hello_world():        	
	
	pickle_in = open("dict.pickle","rb")
	example = pickle.load(pickle_in)	
	return render_template('index.html')
	#return app2.hello_world()
	#return ("hello world")

@app.route('/result',methods = ['POST', 'GET'])
def result():
   	if request.method == 'POST':
    		result = request.form
    		pickle.dump(result, open('dict.pickle','wb'))
    		return render_template("index.html",result = result)

@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
        return jsonify({'result':num*10})
@app.route('/data')
@token_required
def data():
	return jsonify({'message' : 'you have valid token!'})

if __name__ == '__main__':
   app.run(debug=True)
