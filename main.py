from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, logout_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from decouple import config
from flask_bootstrap import Bootstrap5
from forms import *
from db import *
from models import *

app = Flask(__name__)
app.config["SECRET_KEY"] = config("SECRET_KEY")
Bootstrap5(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

# Connect to DB
app.config["SQLALCHEMY_DATABASE_URI"] = config("URI")
db_init(app)

# Initialising Routes
# Main Routes
@app.route("/")
def home():
  return render_template("index.html")

@app.route("/map")
def showMap():
  return "Map"

# Show individual items
@app.route("/profile/<string:username>", methods=["GET","POST"])
def showProfile(username):
  user = db.session.execute(db.select(User).where(User.username == username)).scalar()
  return render_template("profile.html", user=user)

@app.route("/store/<string:store_name>", methods=["GET","POST"])
def showStore(store_name):
  pass

@app.route("/post/<int:post_id>", methods=["GET","POST"])
def showPost(post_id):
  pass

# Manage Stores
@app.route("/<string:username>/stores")
def stores(username):
  username = db.session.execute(db.select(User).where(User.username == username)).scalar()
  return render_template("stores.html",stores=username.stores)

# Create Items
@app.route("/<string:username>/create-store", methods=["GET","POST"])
def addStore(username):
  user = db.session.execute(db.select(User).where(User.username == username)).scalar()
  form = StoreForm()
  if form.validate_on_submit():
    new_store = Store(
      name = form.name.data,
      admin = form.email.data,
      longitude = form.longitude.data,
      latitude = form.latitude.data,
      address = form.address.data
    )
    db.session.add(new_store)
    db.session.commit()
    return redirect(url_for("stores",username=user))
  return render_template("addStore.html",form=form)

@app.route("/create-post", methods=["GET","POST"])
def addPost():
  pass

@app.route("/store/<int:store_id>/create-review", methods=["GET","POST"])
def addReview(store_id):
  pass

@app.route("/store/<int:store_id>/create-announcement", methods=["GET","POST"])
def addAnnouncement(store_id):
  pass

# Delete Items
@app.route("/delete/<int:store_id>")
def delete_store(store_id):
  pass

@app.route("/delete/<int:post_id>")
def delete_post(post_id):
  pass

@app.route("/delete/<int:review_id>")
def delete_review(review_id):
  pass

@app.route("/delete/<int:comment_id>")
def delete_comment(comment_id):
  pass

# User actions
@app.route("/sign-in", methods=["GET","POST"])
def sign_in():
  registerForm = RegisterForm()
  loginForm = LoginForm()
  if registerForm.validate_on_submit():
    user = db.session.execute(db.select(User).where(User.email == registerForm.email.data)).scalar()
    if user:
      flash("You've already signed up with that email, log in instead.")
      return redirect(url_for("sign_in"))
    user = db.session.execute(db.select(User).where(User.username == registerForm.username.data)).scalar()
    if user:
      flash("That username is already taken, please choose another one.")
      return redirect(url_for("sign_in"))

    password = generate_password_hash(
      registerForm.password.data,
      method="pbkdf2:sha256",
      salt_length = 8
    )
    new_user = User(
      email = registerForm.email.data,
      username = registerForm.username.data,
      password = password
    )
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)
    return redirect(url_for("home"))

  if loginForm.validate_on_submit():
    password = loginForm.password.data
    user = db.session.execute(db.select(User).where(User.username == loginForm.username.data)).scalar()
    if not user:
      flash("That username does not exist, please try again.")
      return redirect(url_for("sign_in"))
    elif not check_password_hash(user.password, password):
      flash("Password incorrect, please try again.")
      return redirect(url_for("sign_in"))
    else:
      login_user(user)
      return redirect(url_for("home"))

  return render_template("sign-in.html", registerForm=registerForm, loginForm=loginForm)

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for("home"))

# Running App
if __name__ == "__main__":
  app.run(debug=True)
