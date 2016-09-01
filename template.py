#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from json_parser import JsonParser
import os

app = Flask(__name__)

tasks = [
	{
		'id': 1,
			'title': u'Buy groceries',
			'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
			'done': False
	},
	{
		'id': 2,
		'title': u'Learn Python',
		'description': u'Need to find a good Python tutorial on the web', 
		'done': False
	}
]

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'not Found'}), 404)

@app.route('/test')
def test():
    return "hello world"

@app.route('/tasks/<int:task_id>', methods=['get', 'post'])
def index(task_id):
	task = filter(lambda t:t['id'] == task_id, tasks)
	if len(task) == 0:
		abort(404)
	return jsonify({'task': task})

@app.route('/tasks/postdemo', methods = ['post'])
def postdemo():
	if not request.json or not 'title' in request.json:
		abort(404)	
	task = {
		'title': request.json['title'],
		'description': request.json.get('description','')
	}
	return jsonify({'task': task}), 201

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
