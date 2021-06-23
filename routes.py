from flask import Flask, render_template, request, redirect, url_for, Markup, abort, make_response, session
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%Y_%m_%d_%H_%M_%S")


app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret! (Session)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


my_data={}
@app.route("/")
def home():
    if 'username' in session:
        return render_template('home.html', data=my_data)
    return redirect(url_for('form'))


@app.route("/form")
def form():
    if my_data:
        return redirect(url_for('home'))
    return render_template('form.html')


@app.route("/form2")
def form2():
    # abort(401)
    return render_template('fileForm.html')

@app.route("/set_data", methods=['POST'])
def set_data():
    if request.method == 'POST':
        my_data['name']=request.form['name']
        my_data['email']=request.form['email']
        session['username'] = request.form['name']
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


@app.route('/save_file', methods=['POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('C:/Users/mohamad/Documents/github/Flask-Python/SavedFiles/'+request.form['name']+'_'+current_time+'.txt')
    return redirect(url_for('home'))




@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('page_not_found.html', error=error), 404)
    resp.headers['X-Error'] = 'ERROR BY YOURSELF'
    return resp


if __name__ == "__main__":
    app.run(debug=True)
