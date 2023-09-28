from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('intro.html')

@app.route('/join')
def join():
    return render_template('join.html')