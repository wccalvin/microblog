from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'clayton'}
    posts = [
        {
            'author': {'username': 'clayton'},
            'title': 'Bike path in coventry'
        },
        {
            'author': {'username': 'clayton'},
            'title': 'Thanos'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
