#!coding:utf-8

from flask import Flask

app = Flask(__name__)
@app.route('/project/')
def project():
	return 'The project page'
@app.route('/about')
def about():
	return 'The about page'

if __name__ == '__main__':
	app.run(host="0.0.0.0")

'''
虽然它们看起来确实相似，但它们结尾斜线的使用在 URL 定义 中不同。 第一种情况中，规范的 URL 指向 projects 尾端有一个斜线。 这种感觉很像在文件系统中的文件夹。访问一个结尾不带斜线的 URL 会被 Flask 重定向到带斜线的规范URL去。

然而，第二种情况的 URL 结尾不带斜线，类似 UNIX-like 系统下的文件的路径名。 访问结尾带斜线的 URL 会产生一个 404 “Not Found” 错误。

当用户访问页面时忘记结尾斜线时，这个行为允许关联的 URL 继续工作， 并且与 Apache 和其它的服务器的行为一致。另外，URL 会保持唯一，有助于避免搜索引擎索引同一个页面两次。
'''
