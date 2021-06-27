import sqlite3

import sql
from flask import Flask, render_template, request, redirect, url_for, Markup, abort, make_response, session
import db as pro


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():
    return render_template('testlist.html')

@app.route('/addtask',methods = ['POST', 'GET'])
def addtask():
    data = dict()
    if request.method == 'POST':
        data['body'] = request.form['name']
        data['type'] = 0
        response = pro.insertTask(**data)
        print(response)
        if response[0]:
            return redirect(url_for('home'))
        elif not response[0]:
            abort(404)
    else:
        abort(404)
    return redirect(url_for('home'))


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('page_not_found.html', error=error), 404)
    resp.headers['X-Error'] = 'ERROR BY YOURSELF'
    return resp

if __name__ == "__main__":
    app.run(debug=True)
