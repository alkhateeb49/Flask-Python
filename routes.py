from flask import Flask, render_template, request, redirect, url_for, Markup

app = Flask(__name__)


my_data={}
@app.route("/")
def home():
    return render_template('home.html', data=my_data)

@app.route("/form")
def form():
    if my_data:
        return redirect(url_for('home'))
    return render_template('form.html')

@app.route("/set_data", methods=['POST'])
def set_data():
    if request.method == 'POST':
        my_data['name']=request.form['name']
        my_data['email']=request.form['email']
        return redirect(url_for('home'))

@app.route("/unsetdata")
def unsetData():
    my_data.clear()
    return redirect(url_for('home'))


# @app.route('/user/name1=<value1>&name2=<value2>')
@app.route('/user/')
@app.route('/user/<value1>')
@app.route('/user/name=<value1>&email=<value2>')
def profile(value1=None, value2=None):
    if value1 != None and value2 != None:
        # return f'{username}\'s profile'
        return value1 + ' ' + value2+' profile' + Markup('<br><a href="/">Home</a>')
    return redirect(url_for('home'))


@app.errorhandler(404)
def error(error):
    return render_template('page_not_found.html', error=error), 404



if __name__ == "__main__":
    app.run(debug=True)
