#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from json_parser import JsonParser
import os

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'not Found'}), 404)

class Utils(object):
    def _get_cmd(self, command_list, cmd):
        if cmd not in command_list:
            abort(404)
        return ' ' + cmd

    def _get_opts(self, opts):
        options = ''
	for key in opts.keys():
	    options += ' --' + key + ' ' + opts[key]
        return options

    def _get_args(self, args):
        if len(args) == 0:
            return ''
        return ' ' + args

    def _get_command(self, command_list, cmd, opts, args):
        command = ''
	command += self._get_cmd(command_list, cmd)
        command += self._get_opts(opts)
	command += self._get_args(args)
        return command

    def _exec_command_output(self, command):
	print command
	try:
	    os.system(command)
            result = JsonParser.parse()
            return jsonify(result)
	except Exception, e:
	    print e
            abort(404)
        return None

    def _exec_command_nooutput(self, command):
	print command
	try:
	    os.system(command)
            return jsonify({'state': 'OK'})
	except Exception, e:
	    print e
            abort(404)

    def dispatch_task(self, cmd, opts, args):
	command = 'yardstick task'
        command_list = ['start']
        command += self._get_command(command_list, cmd, opts, args)
        return self._exec_command_output(command)


    def dispatch_runner(self, cmd, opts, args):
	command = 'yardstick runner'
        command_list = ['list', 'show']
        command += self._get_command(command_list, cmd, opts, args)
        return self._exec_command_nooutput(command)

    def dispatch_scenario(self, cmd, opts, args):
	command = 'yardstick scenario'
        command_list = ['list', 'show']
        command += self._get_command(command_list, cmd, opts, args)
        return self._exec_command_nooutput(command)

    def dispatch_testcase(self, cmd, opts, args):
	command = 'yardstick testcase'
        command_list = ['list', 'show']
        command += self._get_command(command_list, cmd, opts, args)
        return self._exec_command_nooutput(command)

    def dispatch_plugin(self, cmd, opts, args):
	command = 'yardstick plugin'
        command_list = ['install', 'remove']
        command += self._get_command(command_list, cmd, opts, args)
        return self._exec_command(command)


utils = Utils()

@app.route('/api/v3/yardstick/<string:main_cmd>/', methods = ['post']) 
def task(main_cmd):
	cmd = request.json.get('cmd', '')
	opts = request.json.get('opts', {})
	args = request.json.get('args', '')

        command_list = ['task', 'runner', 'scenario', 'testcase', 'plugin']
        if main_cmd in command_list:
            method = getattr(utils, 'dispatch_' + main_cmd)
            return method(cmd, opts, args)
        else:
            abort(404)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
