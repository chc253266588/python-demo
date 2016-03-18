#!coding:utf-8

'''
你可以用 cookies 属性来访问 cookies。你能够用响应对象的 set_cookie 来设置 cookies。请求对象中的 cookies 属性是一个客户端发送所有的 cookies 的字典。 如果你要使用会话(sessions)，请不要直接使用 cookies 相反用 Flask 中的 会话，Flask 已经在 cookies 上增加了一些安全细节。
'''

from flask import Flask,render_template,make_response,request

app = Flask(__name__)

#存储 cookies:
@app.route('/')
def index():
	resp = make_response(render_template('hello.html'))
	resp.set_cookie('username','the username')
	return resp
#读取 cookies:
@app.route('/cookie')
def cookie():
	username = request.cookies['username']
	return username

if __name__ == '__main__':
	app.run(host='0.0.0.0')

'''
注意 cookies 是在响应对象中被设置。由于通常只是从视图函数返回字符串， Flask 会将其转换为响应对象。 如果你要显式地这么做，你可以使用 make_response() 函数接着修改它。

有时候你可能要在响应对象不存在的地方设置 cookie。利用 延迟请求回调 模式使得这种情况成为可能。
'''
