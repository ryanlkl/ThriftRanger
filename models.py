from db import db
from sqlalchemy.orm import relationship
from flask_login import UserMixin

# Configure Tables
class Store(db.Model):
  __tablename__ = "stores"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  rating = db.Column(db.Float(2))
  longitude = db.Column(db.Float, nullable=False)
  latitude = db.Column(db.Float, nullable=False)
  address = db.Column(db.String, nullable=False, unique=True)
  mimetype = db.Column(db.Text)
  followers = relationship("User", back_populates="following")
  admin_id = db.Column(db.Integer, db.ForeignKey("users.id"))
  admin = relationship("User", back_populates="stores")
  reviews = relationship("Review", back_populates="parent_store")
  posts = relationship("Post", back_populates="parent_store")
  announcements = relationship("Announcement", back_populates="parent_store")

class Announcement(db.Model):
  __tablename__ = "announcements"
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  mimetype = db.Column(db.Text)
  description = db.Column(db.Text, nullable = False)
  store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
  parent_store = relationship("Store", back_populates="announcements")

class User(UserMixin,db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(50), unique=True, nullable=False)
  password = db.Column(db.String, nullable=False)
  following = relationship("Store", back_populates="followers")
  stores = relationship("Store", back_populates="admin")
  posts = relationship("Post", back_populates="post_author")
  reviews = relationship("Review", back_populates="review_author")
  comments = relationship("Comment", back_populates="comment_author")

class Post(db.Model):
  __tablename__ = "posts"
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(150), nullable=False)
  text = db.Column(db.Text, nullable=False)
  mimetype = db.Column(db.Text)
  store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
  parent_store = relationship("Store", back_populates="posts")
  post_author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
  post_author = relationship("User", back_populates="posts")
  comments = relationship("Comment", back_populates="parent_post")

class Review(db.Model):
  __tablename__ = "reviews"
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(150), nullable=False)
  text = db.Column(db.Text, nullable=False)
  rating = db.Column(db.Integer, nullable=False)
  mimetype = db.Column(db.Text)
  store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
  parent_store = relationship("Store", back_populates="reviews")
  review_author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
  review_author = relationship("User", back_populates="reviews")

class Comment(db.Model):
  __tablename__ = "comments"
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String, nullable=False)
  post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
  parent_post = relationship("Post", back_populates="comments")
  comment_author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
  comment_author = relationship("User", back_populates="comments")
