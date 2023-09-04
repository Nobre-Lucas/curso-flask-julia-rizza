from flask import flash, redirect, render_template, url_for
from flask_login import login_user, logout_user
from app import app
from app import login_manager

from app.models.forms import LoginForm
from app.models.tables import User

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(user.password)
        if user and user.password == form.password.data:
            login_user(user)
            flash('Logged in')
            return redirect(url_for('index'))
        else:
            flash('Login failed')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))