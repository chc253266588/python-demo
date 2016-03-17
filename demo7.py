#!coding:utf-8

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/hello')
def hello(title='HELLO'):
	return render_template('hello.html',title=title)

if __name__ == "__main__":
	app.run(host="0.0.0.0")

'''
在 Python 中生成 HTML 并不好玩，实际上是相当繁琐的，因为你必须自行做好 HTML 转义以保持应用程序的安全。 由于这个原因，Flask 自动为你配置好 Jinja2 模版。

你可以使用方法 render_template() 来渲染模版。所有你需要做的就是提供模版的名称以及你想要作为关键字参数传入模板的变量。

Flask 将会在 templates 文件夹中寻找模版。因此如果你的应用是个模块，这个文件夹在模块的旁边，如果它是一个包，那么这个文件夹在你的包里面

对于模板，你可以使用 Jinja2 模板的全部功能。

在模版中你也可以使用 request, session 和 g [1] 对象，也能使用函数 get_flashed_messages() 。

模版继承是十分有用的。如果想要知道模版继承如何工作的话，请阅读文档 模板继承 。基本的模版继承使得某些特定元素（如标题，导航和页脚）在每一页成为可能。

自动转义是开启的，因此如果 name 包含 HTML，它将会自动转义。如果你信任一个变量，并且你知道它是安全的 （例如一个模块把 wiki 标记转换到 HTML ），你可以用 Markup 类或 |safe 过滤器在模板中标记它是安全的。 在 Jinja 2 文档中，你会见到更多例子。

'''
