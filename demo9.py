#!coding:utf-8
from flask import Flask,request,redirect,url_for
from werkzeug import secure_filename
from flask import send_from_directory
import os

UPLOAD_FOLDER = '/tmp/uploads'
ALLOWED_EXTENSIONS = set(['txt','pdf','png','jpg','jpeg','gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/',methods=['GET','POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
			return redirect(url_for('uploaded_file',filename=filename))
	return '''
	<!doctype html>
	<title>Upload new File</title>
	<h1>Upload new File</h1>
	<form action="" method=post enctype=multipart/form-data>
		<p><input type=file name=file>
		<input type=submit value=Upload />
	</form>
	'''
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == "__main__":
	app.run(host='0.0.0.0')

'''
你能够很容易地用 Flask 处理文件上传。只要确保在你的 HTML 表单中不要忘记设置属性 enctype="multipart/form-data"， 否则浏览器将不传送文件。

上传的文件是存储在内存或者文件系统上一个临时位置。你可以通过请求对象中 files 属性访问这些文件。 每个上传的文件都会存储在这个属性字典里。它表现得像一个标准的 Python file 对象，但是它同样具有 save() 方法，该方法允许你存储文件在服务器的文件系统上。 
如果你想要知道在上传到你的应用之前在客户端的文件名称，你可以访问 filename 属性。但请记住永远不要信任这个值，因为这个值可以伪造。如果你想要使用客户端的文件名来在服务器上存储文件， 把它传递到 Werkzeug 提供给你的 secure_filename() 函数

werkzeug.secure_filename() 会 在稍后解释。UPLOAD_FOLDER 是上传文件要储存的目录，ALLOWED_EXTENSIONS 是允许 上传的文件扩展名的集合。接着我们给应用手动添加了一个 URL 规则。一般现在不会做 这个，但是为什么这么做了呢？原因是我们需要服务器（或我们的开发服务器）为我们提供 服务。因此我们只生成这些文件的 URL 的规则。

为什么要限制文件件的扩展名呢？如果直接向客户端发送数据，那么你可能不会想让用户 上传任意文件。否则，你必须确保用户不能上传 HTML 文件，因为 HTML 可能引起 XSS 问题（参见 跨站脚本攻击（XSS） ）。
那么 secure_filename() 函数到底是有什么用？有一条原则是“ 永远不要信任用户输入”。这条原则同样适用于已上传文件的文件名。所有提交的表单数据 可能是伪造的，文件名也可以是危险的。此时要谨记：在把文件保存到文件系统之前总是要 使用这个函数对文件名进行安检。
现在还剩下一件事：为已上传的文件提供服务。 Flask 0.5 版本开始我们可以使用一个 函数来完成这个任务: send_from_directory
'''
