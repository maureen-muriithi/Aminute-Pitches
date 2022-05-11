from flask import render_template, redirect, url_for, flash, request
from . import auth
from flask_login import login_user
from ..models import User
from .forms import LoginForm, RegisterForm
from .. import db


@auth.route('/login')
def login():
    return render_template('auth/login.html')

@auth.route('/register', methods =  ["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit:
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)

@auth.rout('/login', methods = ["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit:
        user = User.query.filter_by(username = login_form.username.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "watchlist login"
    return render_template('auth/login.html',login_form = login_form,title=title)