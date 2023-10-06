from flask import Flask, render_template, request, redirect, url_for, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from decouple import config
from flask_bootstrap import Bootstrap5
from sqlalchemy.orm import relationship
from functools import wraps

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
db = SQLAlchemy()
db.init_app(app)

# Configure Tables
class Store(db.Model):
  __tablename__ = "stores"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  rating = db.Column(db.Float(2), nullable=False)
  longitude = db.Column(db.Float, nullable=False)
  latitude = db.Column(db.Float, nullable=False)
  reviews = relationship("Review", back_populates="parent_store")
  posts = relationship("Post", back_populates="parent_store")

class User(UserMixin,db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(50), unique=True, nullable=False)
  password = db.Column(db.String, nullable=False)
  first_name = db.Column(db.String(20), nullable=False)
  last_name = db.Column(db.String(20))
  posts = relationship("Post", back_populates="post_author")
  reviews = relationship("Review", back_populates="review_author")

class Post(db.Model):
  __tablename__ = "posts"
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(150), nullable=False)
  text = db.column(db.Text, nullable=False)
  store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
  parent_store = relationship("Store", back_populates="posts")
  post_author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
  post_author = relationship("User", back_populates="posts")

class Review(db.Model):
  __tablename__ = "reviews"
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(150), nullable=False)
  text = db.Column(db.Text, nullable=False)
  rating = db.Column(db.Integer, nullable=False)
  store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
  parent_store = relationship("Store", back_populates="reviews")
  review_author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
  review_author = relationship("User", back_populates="reviews")

class Comments(db.Model):
  __tablename__ = "comments"

with app.app_context():
  db.create_all()

# Initialising Routes

# Main Routes
@app.route("/")
def home():
  return render_template("index.html")

@app.route("/map")
def showMap():
  return "Map"

# Show individual items
@app.route("/profile/<int:user_id>", methods=["GET","POST"])
def showProfile(user_id):
  pass

@app.route("/store/<int:store_id>", methods=["GET","POST"])
def showStore(store_id):
  pass

@app.route("/post/<int:post_id>", methods=["GET","POST"])
def showStore(post_id):
  pass

# Delete Items
@app.route("delete/<int:store_id>")
def delete_store(store_id):
  pass

@app.route("delete/<int:post_id>")
def delete_post(post_id):
  pass

@app.route("delete/<int:review_id>")
def delete_review(review_id):
  pass

@app.route("delete/<int:comment_id>")
def delete_comment(comment_id):
  pass

# User actions
@app.route("sign-in", methods=["GET","POST"])
def sign_in():
  pass

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for("home"))

# Running App
if __name__ == "__main__":
  app.run(debug=True)
