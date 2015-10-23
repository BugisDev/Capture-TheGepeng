from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from flask.views import MethodView
from flask.ext.login import current_user, login_user, login_required, logout_user
from form import UserLoginForm

#blueprint for User ==> views
user_views = Blueprint('user', __name__, template_folder='../../templates', static_folder='../../static')

@user_views.route('/')
@login_required
def home():
    return render_template('index.html')

@user_views.route('/welcome')
def welcome():
    return render_template('welcome.html')

class UserLogin(MethodView):

    def get(self):
        form = UserLoginForm(request.form)
        return render_template('login.html', **context)

    def post(self):
        form = UserLoginForm(request.form)
        context = {
            'form': form,
            'error': None
        }
        if form.validate_on_submit():
            user = form.validate_login()
            if user:
                login_user(user)
                return redirect(url_for('user.home'))
            else:
                context['error'] = 'Invalid Username / Password.'
        return render_template('login.html', **context)

user_views.add_url_rule('/login', view_func=UserLogin.as_view('login'))

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
