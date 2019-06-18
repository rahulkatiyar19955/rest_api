from flask import Flask, redirect, url_for
import os
app = Flask(__name__)

@app.route('/')
def func():
    return 'Hello World Rahul!'

@app.route('/admin')
def admin():
    return 'You have admin access ' + name

@app.route('/<string:nam>')
def name1(name):
    if(name[0]== 'A' or name[0] == 'a'):
        return redirect(url_for('admin'))
    return 'hello  ' + name

portno = os.environ.get('PORT')
app.run(port=portno,host= '0.0.0.0',debug = True)
