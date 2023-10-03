from flask import render_template, flash, redirect, url_for 
from app import app
from app.forms import SignupForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('intro.html', title ='Wehive: Home')

@app.route('/join', methods=['GET','POST'])
def join():
    form = SignupForm()
    if form.validate_on_submit ():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('join.html', title = 'Join Wehive', form=form)
    
