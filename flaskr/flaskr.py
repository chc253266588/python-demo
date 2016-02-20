#!coding:utf-8

import sqlite3
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = '123456'

#用同一文件(在 flaskr.py 中)中的配置初始化

app = Flask(__name__)
app.config.from_object(__name__)

'''
from_object() 将会寻找给定的对象(如果它是一个字符串，则会导入它)， 搜寻里面定义的全部大写的变量。在我们的这种情况中，配置文件就是我们上面写的几行代码。 你也可以将他们分别存储到多个文件。

通常，从配置文件中加载配置是一个好的主意。这是 from_envvar() 所做的， 用它替换上面的 from_object()

app.config.from_envvar('FLASKR_SETTINGS', silent=True)
这种方法我们可以设置一个名为 FLASKR_SETTINGS 环境变量来设定一个配置文件载入后是否覆盖默认值。 静默开关告诉 Flask 不去关心这个环境变量键值是否存在。

secret_key 是需要为了保持客户端的会话安全。明智地选择该键，使得它难以猜测，尽可能复杂。 调试标志启用或禁用交互式调试。决不让调试模式在生产系统中启动，因为它将允许用户在服务器上执行代码！

我们还添加了一个轻松地连接到指定数据库的方法，这个方法用于在请求时打开一个连接，并且在交互式 Python shell 和脚本中也能使用。
'''

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
	g.db = connect_db()
@app.teardown_request
def teardown_request(exception):
	g.db.close()

@app.route('/')
def show_entries():
	cur = g.db.execute('select title,text from entries order by id desc')
	entries = [dict(title=row[0],text=row[1]) for row in cur.fetchall()]
	return render_template('show_entries.html',entries=entries)

@app.route('/add',methods=['POST'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)
	g.db.execute('insert into entries (title,text) values (?,?)',[request.form['title'],request.form['text']])
	g.db.commit()
	flash('New entry was successfully posted')
	return redirect(url_for('show_entries'))

@app.route('/login',methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			flash('You were logger in')
			return redirect(url_for('show_entries'))
	return render_template('login.html',error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in',None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))

if __name__ == '__main__':
	app.run(host='0.0.0.0')


