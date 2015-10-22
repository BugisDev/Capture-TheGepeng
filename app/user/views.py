from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from functools import wraps
from form import LoginForm
from flask.ext.bcrypt import Bcrypt

#blueprint for User ==> views
user_views = Blueprint('user', __name__, template_folder='../../templates', static_folder='../../static')


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('user.login'))
    return wrap


@user_views.route('/')
@login_required 
def home():
    return render_template('index.html')


@user_views.route('/welcome')
def welcome():
    return render_template('welcome.html')


@user_views.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            if request.form['username'] != 'admin' or request.form['password'] != 'admin':
                error = 'Invalid credintials. Please try again.'
            else:
                session['logged_in'] = True
                flash('You were just logged in!')
                return redirect(url_for('user.home'))
        else:
            render_template('login.html', form=form, error=error)
    return render_template('login.html', form=form, error=error)

@user_views.route("/register", methods=['GET', 'POST'])
def register():
    error=None
#    if request.method == 'POST':
#        if request.form(['username'] or [''] 
    return render_template('register.html', error=error)

@user_views.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('user.login'))

@user_views.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404