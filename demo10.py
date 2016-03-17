#!coding:utf-8

#你能够用 redirect() 函数重定向用户到其它地方。能够用 abort() 函数提前中断一个请求并带有一个错误代码。

from flask import Flask,url_for,abort,redirect,render_template

app = Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for('login'))

@app.route('/login')
def login():
	abort(401)
	this_is_never_executed()

#默认情况下，每个错误代码会显示一个黑白错误页面。如果你想定制错误页面，可以使用 errorhandler() 装饰器:
@app.errorhandler(401)
def page_not_found(error):
	return render_template("page_not_found.html",error=error)
#注意到 404 是在 render_template() 调用之后。告诉 Flask 该页的错误代码应是 404 ， 即没有找到。默认的 200 被假定为：一切正常。

if __name__ == "__main__":
	app.run(host="0.0.0.0")
