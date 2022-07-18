
import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user')
def user():
    return 'user called'

@app.route('/user/<username>/<int:age>')
def user_1(username,age):
    return f'{username} 님의 나이는 {age+1} 입니다.'

@app.route('/customer')
def customer():
    print('name:',request.args.get('name'))
    print('age:',request.args.get('age'))
    return 'customer called'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("form_input.html")
    else:
        # return f"login: {request.form['username']} {request.form['password']}"
        return render_template('form_result.html',result=request.form)

@app.route('/fileupload',methods=['GET','POST'])
def fileupload():
    if request.method=='GET':
        return render_template('fileupload.html')
    else:
        f = request.files['file']
        path = os.path.dirname(__file__)+'/upload/'+f.filename
        print(path)
        f.save(path)
        return redirect('/')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80,debug=True)


