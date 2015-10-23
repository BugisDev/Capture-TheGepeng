from flask_wtf import Form
from wtforms import validators,PasswordField, StringField
from wtforms.validators import DataRequired
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
#from auth import bcrypt


#User Login Form
class UserLoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

    def validate_login(self):
        user = self.get_user()

        if user is None:
            # raise validators.ValidationError('Invalid User')
            return False

        if not check_password_hash(user.password, self.password.data):
            # raise validators.ValidationError('Invalid Password')
            return False

        return user

    def get_user(self):
        return db.session.query(User).filter_by(username=self.username.data).first()
        return db.session.query(User).filter_by(password=self.password.data).first()


#Register Login Form
class UserRegisterForm(Form):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])

    password = PasswordField('password', validators=[DataRequired()])
    password = PasswordField('password', [
        validators.Required(),
        validators.EqualTo('password_confirm', message='Passwords must match')
    ])
    password_confirm = PasswordField('Repeat Password')

