from flask import Blueprint, render_template, redirect, url_for, request

user_views = Blueprint('user', __name__, template_folder='../../templates')


@user_views.route("/user/login", methods=['GET', 'POST'])
def user_login():
    error = None
    # handle get method
    if request.method == 'POST' :
        if request.form['username'] == 'admin' and request.form['password'] =='admin':
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            error = 'Invalid credintials. Please try again.'

    return render_template('login.html', error=error #+ **locals())

#@user_views.route('/logout')
#def logout():
#    session.pop('logged_in', None)
#    return redirect(url_for('welcome'))