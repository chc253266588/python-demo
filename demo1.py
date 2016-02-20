#!coding:utf-8
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
	return "hello world!"

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0',port=80)

#首先我们导入了类 Flask 。这个类的实例化将会是我们的 WSGI 应用。第一个参数是应用模块的名称。 如果你使用的是单一的模块（就如本例），第一个参数应该使用 __name__。因为取决于如果它以单独应用启动或作为模块导入， 名称将会不同 （ '__main__' 对应于实际导入的名称）。获取更多的信息，请阅读 Flask 的文档。
#接着，我们创建一个该类的实例。我们传递给它模块或包的名称。这样 Flask 才会知道去哪里寻找模板、静态文件等等。
#我们使用装饰器 route() 告诉 Flask 哪个 URL 才能触发我们的函数。
#定义一个函数，该函数名也是用来给特定函数生成 URLs，并且返回我们想要显示在用户浏览器上的信息。
#最后我们用函数 run() 启动本地服务器来运行我们的应用。if __name__ == '__main__': 确保服务器只会在该脚本被 Python 解释器直接执行的时候才会运行，而不是作为模块导入的时候。
#app.run(host='0.0.0.0') 这让你的操作系统去监听所有公开的 IP。
#app.run(debug=True)  调试模式
#port=80   设置对外端口  默认是5000
