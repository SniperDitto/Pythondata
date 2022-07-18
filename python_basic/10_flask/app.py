import os
from flask import Flask,request,redirect,render_template
import sqlite3

app = Flask(__name__)
path = os.path.dirname(__file__)
# conn = sqlite3.connect(path+'/customer.db')
# cur = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inputform',methods=['GET','POST'])
def inputform():
    if request.method=='GET':
        return render_template('inputform.html')
    else:
        # db에 데이터 저장 로직 여기에
        conn = sqlite3.connect(path+'/customer.db')
        cur = conn.cursor()
        cur.execute('''
                CREATE TABLE IF NOT EXISTS CUSTOMER(
                        NAME TEXT,
                        EMAIL TEXT,
                        TEL TEXT,
                        ADDRESS TEXT,
                        GENDER TEXT
                    )
            ''')
        conn.commit()
        data=[request.form['name'],request.form['email'],request.form['tel'],request.form['address'],request.form['gender']]
        cur.execute('INSERT INTO CUSTOMER VALUES(?,?,?,?,?)',data)
        conn.commit()
        conn.close()
        return redirect('/')

@app.route('/customerlist')
def customerlist():
    conn = sqlite3.connect(path+'/customer.db')
    cur = conn.cursor()
    cur.execute('select * from customer order by name')
    data = cur.fetchall()
    return render_template('customerlist.html',data=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=80)
