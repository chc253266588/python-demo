#!coding:utf-8

'''
除了请求对象，还有第二个称为 session 对象允许你在不同请求间存储特定用户的信息。 这是在 cookies 的基础上实现的，并且在 cookies 中使用加密的签名。这意味着用户可以查看 cookie 的内容， 但是不能修改它，除非它知道签名的密钥。
'''

from flask import Flask,session,redirect,url_for,escape,request

app = Flask(__name__)

@app.route('/')
def index():
	if 'username' in session:
		return 'logged in as %s' % escape(session['username'])
		#这里提到的 escape() 可以在你不使用模板引擎的时候做转义（如同本例）。
	return 'You are not logger in'

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index'))
	return '''
		<form action='' method='post'>
			<p><input type='text' name='username' \>
			<p><input type='submit' value='Login' \>
		</form>
	'''

@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect(url_for('index'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
'''
随机的问题在于很难判断什么是真随机。一个密钥应该足够随机。你的操作系统可以基于一个密码随机生成器来生成漂亮的随机值，这个值可以用来做密钥:
>>> import os
>>> os.urandom(24)
'\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
'''
if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
