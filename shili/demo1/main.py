#coding:utf-8

from flask import Flask,render_template,url_for,flash,request,redirect,session,abort
import sqlite3

app = Flask(__name__)
app.secret_key='253266588'

ADMIN = ['chenhc','admin','lobo']

@app.route('/')
def index():
	return render_template('index.html')	

@app.route('/index')
def index2():
	if not session.get('user'):
		abort(401)
	return render_template('index2.html')

@app.route('/login/',methods=['POST','GET'])
def login():
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		conn = sqlite3.connect('/tmp/demo1.db')
		cursor = conn.cursor()
		sql = "select * from users where username='%s' and password='%s'" % (username,password)
		cursor.execute(sql)
		result = cursor.fetchall()
		cursor.close()
		conn.close()
		if result:
			session['user'] = username
			return redirect(url_for('index2'))
		else:
			flash("username or password is error!")
	return render_template('login.html')	
@app.route('/logout')
def logout():
	session.pop('user',None)
	return redirect(url_for('index'))

@app.errorhandler(401)
def page_not_found(error):
    return render_template('page_not_found.html'), 401

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0',port=80)
