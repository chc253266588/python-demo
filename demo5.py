#!coding:utf-8

from flask import Flask,request

app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		do_the_login()
	else:
		show_the_login_form()

'''
HTTP (也就说 web 应用协议)有不同的方法来访问 URLs。默认情况下，路由只会响应 GET 请求， 但是能够通过给 route() 装饰器提供 methods 参数来改变。
如果使用 GET 方法，HEAD 方法将会自动添加进来。你不必处理它们。也能确保 HEAD 请求 会按照 HTTP RFC (文档在 HTTP 协议里面描述) 要求来处理， 因此你完全可以忽略这部分 HTTP 规范。 同样地，自从 Flask 0.6 后，OPTIONS 也能自动为你处理。
HTTP 方法（通常也称为“谓词”）告诉服务器客户端想要对请求的页面 做 什么。下面这些方法是比较常见的：

GET
浏览器通知服务器只 获取 页面上的信息并且发送回来。这可能是最常用的方法。
HEAD
浏览器告诉服务器获取信息，但是只对 头信息 感兴趣，不需要整个页面的内容。 应用应该处理起来像接收到一个 GET 请求但是不传递实际内容。在 Flask 中你完全不需要处理它， 底层的 Werkzeug 库会为你处理的。
POST
浏览器通知服务器它要在 URL 上 提交 一些信息，服务器必须保证数据被存储且只存储一次。 这是 HTML 表单通常发送数据到服务器的方法。
PUT
同 POST 类似，但是服务器可能触发了多次存储过程，多次覆盖掉旧值。现在你就会问这有什么用， 有许多理由需要如此去做。考虑下在传输过程中连接丢失：在这种情况下浏览器 和服务器之间的系统可能安全地第二次接收请求，而不破坏其它东西。对于 POST 是不可能实现的，因为 它只会被触发一次。
DELETE
移除给定位置的信息。
OPTIONS
给客户端提供一个快速的途径来指出这个 URL 支持哪些 HTTP 方法。从 Flask 0.6 开始，自动实现了它。
'''
