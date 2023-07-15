from flask import Blueprint, request, render_template, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from website import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        Email = request.form.get('email')
        Password = request.form.get('password')
        user = User.query.filter_by(email = Email).first()
        if user:
            if check_password_hash(user.password,Password):
                flash("Logged in successfully", category='success')
                login_user(user)
                return redirect(url_for('views.home'))
            else:
                flash("Password Wrong, Please try again", category='error')
        else:
            flash("Email does not exists", category="error")
    return render_template("login.html", user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route('/signup', methods=["GET", "POST"])
def signup():
    print("yashyashyash")
    if request.method == "POST":
        email = request.form.get("email")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        password = request.form.get("password")

        user = User.query.filter_by(email = email).first()
        if user:
            flash("User already exists", category="error")
        elif len(email) < 3:
            flash('Email must be greater than 3 character', category='error')
        elif len(firstname) <= 2:
            flash('Firstname must be greater or equal to 3 character', category='error')
        elif len(lastname) < 3:
            flash('Lastname must be greater than 3 character', category='error')
        elif len(password) < 5:
            flash('Password must be greater than 5', category='error')
        else:
            new_user = User(email = email, firstname = firstname, lastname = lastname, password = generate_password_hash(password,method = 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Form successfull got it', category='success')
            return redirect(url_for('views.home'))

                                                                                                                            
    return render_template("signup.html", user = current_user)