from flask import abort,Flask,render_template,redirect,session,request,flash

app = Flask(__name__)
ADMIN = ['chenhc','admin','lobo']
app.secret_key = 'hello world'

@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method=='POST':
		username = request.form.get('username')
		if username in ADMIN:
			session['username'] = username
			return redirect('/')
		else:
			flash("username is error!")
	return render_template('login.html')
	
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/test')
def test():
	return render_template('test.html')
@app.route("/logout/")
def logout():
	session.pop('username')
	return redirect('/')


if __name__ == "__main__":
	app.debug=True
	app.run(host='0.0.0.0',port=80)


