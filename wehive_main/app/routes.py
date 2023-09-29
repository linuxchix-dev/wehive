from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('intro.html', title ='Wehive: Home')

@app.route('/join')
def join():
    form = SignupForm()
    return render_template('join.html', title = 'Join Wehive', form=form)
