from flask import Flask, redirect, url_for
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



app.run(port=5000,debug = True)
