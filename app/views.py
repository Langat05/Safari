from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    title = 'Welcome to Africa'
    return render_template('index.html', title = title)