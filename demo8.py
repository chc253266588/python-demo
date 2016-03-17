#!coding:utf-8

from flask import request
'''当前请求的方法可以用 method 属性来访问。你可以用 form 属性来访问表单数据 (数据在 POST 或者 PUT 中传输)。这里是上面提及到两种属性的完整的例子:'''

@app.route('/login', methods=['POST', 'GET'])
def login():
	error = None
	if request.method == 'POST':
		if valid_login(request.form['username'],request.form['password']):
			return log_the_user_in(request.form['username'])
		else:
			error = 'Invalid username/password'
			# the code below this is executed if the request method
			# was GET or the credentials were invalid
	return render_template('login.html', error=error)


#你可以用 args 属性来接收在 URL ( ?key=value ) 中提交的参数:
searchword = request.args.get('key', '')
