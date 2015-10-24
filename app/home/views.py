from flask import Blueprint, render_template, redirect, url_for, request, session, flash, Response
from flask.views import MethodView
from app.user.views import user_views, login_required, logout_user


home_views = Blueprint('home', __name__, template_folder='../../templates', static_folder='../../static')