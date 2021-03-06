from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

# web forms



class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


# Using Template rendering
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     name = None
#     form = NameForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         form.name.data = ''
#     return render_template('index.html', form=form, name=name)

# user session
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         old_name = session.get('name')
#         if old_name is not None and old_name != form.name.data:
#             flash('Looks like you have changed your name!')
#         session['name'] = form.name.data
#         form.name.data = ''
#         return redirect(url_for('index'))
#     return render_template('index.html',
#         form = form, name = session.get('name'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# customize error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Moment
moment = Moment(app)

# Add datetime variable
@app.route('/index2')
def index2():
    return render_template('index2.html', current_time=datetime.utcnow())

# @app.route('/')
# def index():
#     return '<h1>Hello World!</h1>'
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import abort
# @app.route('/')
# def index():
#     return redirect('http://www.example.com')

# from flask import redirect
#
# @app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1>Hello, %s</h1>' % user.name

# ...
bootstrap = Bootstrap(app)
if __name__ == '__main__':
    app.run(debug=True)
