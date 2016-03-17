#!coding:utf-8

from flask import Flask,url_for
app = Flask(__name__)
@app.route('/')
def index():
	img = url_for('static',filename='style.css')
	return img

if __name__ == '__main__':
	app.run(host='0.0.0.0')

'''
动态的 web 应用同样需要静态文件。CSS 和 JavaScript 文件通常来源于此。理想情况下， 你的 web 服务器已经配置好为它们服务，然而在开发过程中 Flask 能够做到。 只要在你的包中或模块旁边创建一个名为 static 的文件夹，在应用中使用 /static 即可访问。
'''
