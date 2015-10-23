import datetime
from app.core.db import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    created = db.Column(db.DateTime())

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def get_fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_id(self):
        return unicode(self.id)

    def is_anonymous(self):
        return False

    def __init__(self, username, email, password, first_name, last_name):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.first_name = first_name
        self.last_name = last_name
        if self.id is None:
            self.created = datetime.datetime.utcnow()

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @property
    def full_name(self):
        return self.get_fullname()
