#!coding:utf-8

from flask import Flask, url_for
app = Flask(__name__)
@app.route('/')
def index(): pass
@app.route('/login')
def login(): pass
@app.route('/user/<username>')
def profile(username): pass
with app.test_request_context():
	print url_for('index')
	print url_for('login')
	print url_for('login', next='/')
	print url_for('profile', username='John Doe')

'''
(这里也使用了 test_request_context() 方法，下面会给出解释。这个方法告诉 Flask 表现得像是在处理一个请求)。

为什么你愿意构建 URLs 而不是在模版中硬编码？这里有三个好的理由：

1.反向构建通常比硬编码更具备描述性。更重要的是，它允许你一次性修改 URL， 而不是到处找 URL 修改。
2.构建 URL 能够显式地处理特殊字符和 Unicode 转义，因此你不必去处理这些。
3.如果你的应用不在 URL 根目录下(比如，在 /myapplication 而不在 /)， url_for() 将会适当地替你处理好。
'''
