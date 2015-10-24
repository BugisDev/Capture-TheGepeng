from flask import Blueprint, render_template, redirect, url_for, request, session, flash, Response
from flask.views import MethodView
from flask.ext.login import  LoginManager, current_user, login_user, login_required, logout_user, current_app
from form import UserLoginForm, UserRegisterForm
from models import User, db
#from app.news.views import news_views


#blueprint for User ==> views
user_views = Blueprint('user', __name__, template_folder='../../templates', static_folder='../../static')


login_manager = LoginManager
login_manager.login_view = "user.login"

@user_views.route('/')
def index():
    return render_template('index.html')

@user_views.route('/home')
@login_required
def home():
    return render_template('home.html')

        

##############For Login Form#################
class UserLogin(MethodView):
    def get(self):
        if current_user.is_authenticated:
            return redirect('/')
        form = UserLoginForm(request.form)
        context = {
            'form': form,
            'error': None
        }
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
                #context['error'] = 'Invalid Username / Password.'
                error = 'Invalid Username / Password.'
        return render_template('login.html', **context)

##Route /Login###
user_views.add_url_rule('/login', view_func=UserLogin.as_view('login'))


####################For register Form######################

class UserRegister(MethodView):
    ####handle GET method
    def get(self):
        form = UserRegisterForm(request.form)
        context = {
            'form': form,
            'error': None
        }
        return render_template('register.html', **context)
    
    ####handle POST method
    def post(self):
        form = UserRegisterForm(request.form)
        context = {
            'form': form,
            'error': None
        }
        
        if form.validate_on_submit():
            user = User(form.first_name.data, 
                        form.last_name.data, 
                        form.username.data, 
                        form.email.data, 
                        form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Thanks for registering')
            error = 'something wrong'
            return redirect(url_for('user.login'))
        return render_template('register.html', **context)

##Route /Register###
user_views.add_url_rule('/register', view_func=UserRegister.as_view('register'))

#For logout route
@user_views.route("/logout")
@login_required
def logout():
    logout_user()
 #     flash ('You\'re Logged Out')
    return redirect(url_for('user.login'))





@user_views.errorhandler(401)
def custom_401(error):
    return render_template('401.html')


@user_views.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404
