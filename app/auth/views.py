from flask import render_template, redirect, url_for, flash, request
from . import auth
from flask_login import login_user, logout_user, login_required
from ..models import User
from .forms import LoginForm, RegisterForm
from .. import db
# from ..email import mail_message


@auth.route('/register', methods =  ["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user = User(email = email, username = username, password = password)
        db.session.add(user)
        db.session.commit()
        
        # mail_message("Welcome to Amminute Pitches","email/welcome_user",user.email,user=user)
        
        return redirect(url_for('auth.login'))
    title = "Register for Aminute app"
    return render_template('auth/register.html',register_form = form, title = title)

@auth.route('/login', methods = ["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit:
        user = User.query.filter_by(username = login_form.username.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "pitches-app login"
    return render_template('auth/login.html',login_form = login_form, title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))