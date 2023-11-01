from db import *
from models import *
from flask import flash, redirect, url_for
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

class UserFunctions:
  def createUser(email,username,password):
    # Check if email exists or not
    user = db.session.execute(db.select(User).where(User.email == email)).scalar()
    if user:
      flash("You've already signed up with that email, log in instead.")
      return redirect(url_for("sign_in"))

    # Check if username exists or not
    user = db.session.execute(db.select(User).where(User.email == username)).scalar()
    if user:
      flash("That username is already taken, please choose another one.")
      return redirect(url_for("sign_in"))

    # Create password encryption
    password = generate_password_hash(
      password,
      method="pbkdf2:sha256",
      salt_length=8
    )

    # Create new User
    new_user = User(
      email = email,
      username = username,
      password = password
    )
    # Update DB
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)
    return

  def logInUser(username,password):
    user = db.session.execute(db.select(User).where(User.username == username)).scalar()

    # Checks whether user exists or not
    if not user:
      flash("That username does not exist, please try again.")
      return redirect(url_for("sign_in"))
    # Checks whether password matches or not
    elif not check_password_hash(user.password, password):
      flash("Password incorrect, please try again.")
      return redirect(url_for("sign_in"))
    # All conditions met, so the user is logged in
    else:
      login_user(user)
      return redirect(url_for("home"))

  def logOutUser():
    logout_user()
    return redirect(url_for("home"))
