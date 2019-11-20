from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email,EqualTo
from .models import User

class LoginForm(FlaskForm):
    username = StringField('Username',render_kw={"placeholder": "Username"}, validators=[DataRequired()])
    password = PasswordField('Password', render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit= SubmitField('Sign In')

class SignupForm(FlaskForm):    
    username = StringField('Username',render_kw={"placeholder": "Username"},validators=[DataRequired()])
    email = StringField('Email', render_kw={"placeholder": "you@example.com"},validators=[DataRequired()])
    role = StringField('Role', render_kw={"placeholder": "Role"},validators=[DataRequired()])
    password = PasswordField('Password',render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password', render_kw={"placeholder": "Confirm Password"}, validators=[DataRequired(), EqualTo('password')])
    remember_me = BooleanField('Remember Me')
    submit= SubmitField('Register User')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


# class AdminForm(FlaskForm):
    
#     Adminusername = StringField('Username', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirmpassword = PasswordField('Confirm Password', validators=[DataRequired()])
#     remember_me = BooleanField('Remember Me')
#     submit= SubmitField('Sign In')


# class RegistrationForm(FlaskForm):
#     username = StringField('Username', render_kw={"placeholder": "Username"},validators=[DataRequired()])
#     email = StringField('Email',render_kw={"placeholder": "Email"}, validators=[DataRequired()])
#     role = StringField('Role', render_kw={"placeholder": "Role"},validators=[DataRequired()])
#     password = PasswordField('Password',render_kw={"placeholder": "Password"}, validators=[DataRequired()])
#     confirmpassword = PasswordField(
#         'Confirm Password',render_kw={"placeholder": "Confirm Password"}, validators=[DataRequired(), EqualTo('password')])
#     remember_me = BooleanField('Remember Me')
#     submit = SubmitField('Register User')

#     def validate_username(self, username):
#         user = User.query.filter_by(username=username.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different username.')

#     def validate_email(self, email):
#         user = User.query.filter_by(email=email.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different email address.')

