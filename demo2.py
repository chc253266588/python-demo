#!coding:utf-8

from flask import Flask
app = Flask(__name__)
@app.route('/user/<username>')
def show_user_profile(username):
	return 'User is %s' % username
@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post is %d' % post_id

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')


'''变量规则
为了给 URL 增加变量的部分，你需要把一些特定的字段标记成 <variable_name>。这些特定的字段将作为参数传入到你的函数中。当然也可以指定一个可选的转换器通过规则 <converter:variable_name>。
'''
