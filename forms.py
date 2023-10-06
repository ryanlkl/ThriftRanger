from wtforms import StringField, FloatField, SubmitField, EmailField, PasswordField, BooleanField, URLField
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired()])
  password = PasswordField("Password", validators=[DataRequired()])
  submit = SubmitField("Login", render_kw={
    'class':'primary-button'
    })


class RegisterForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired()])
  email = EmailField("Email", validators=[DataRequired()])
  password = PasswordField("Password", validators=[DataRequired()])
  submit = SubmitField("Sign Up", render_kw={
    'class':'primary-button'
    })

class StoreForm(FlaskForm):
  name = StringField("Store Name", validators=[DataRequired()])
  address = StringField("Address", validators=[DataRequired()])
  longitude = FloatField("Longitude", validators=[DataRequired()])
  latitude = FloatField("Latitude", validators=[DataRequired()])
  submit = SubmitField("Set Up", render_kw={
    'class':'primary-button'
    })

class AnnouncementForm(FlaskForm):
  title = StringField("Title", validators=[DataRequired()])
  text = CKEditorField("Text", validators=[DataRequired()])
  submit = SubmitField("Post", render_kw={
    'class':'primary-button'
    })

class PostForm(FlaskForm):
  title = StringField("Title", validators=[DataRequired()])
  text = CKEditorField("Text", validators=[DataRequired()])
  submit = SubmitField("Post", render_kw={
    'class':'primary-button'
    })

class ReviewForm(FlaskForm):
  title = StringField("Title", validators=[DataRequired()])
  rating = FloatField("Rating", validators=[DataRequired()])
  text = CKEditorField("Text", validators=[DataRequired()])
  submit = SubmitField("Post", render_kw={
    'class':'primary-button'
    })
