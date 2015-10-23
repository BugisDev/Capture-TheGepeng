from flask_wtf import Form
from wtforms import validators
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired

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
