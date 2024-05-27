from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo

#creates the login information
class LoginForm(FlaskForm):
    userName=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")
 
 # this is the registration form
class RegisterForm(FlaskForm):
    userName=StringField("User Name", validators=[InputRequired()])
    emailid = StringField("Email Address", validators=[Email("Please enter a valid email")])
    contactNumber=StringField("Contact Number", validators=[InputRequired(), Length(max=11)])
    address=StringField("Address", validators=[InputRequired()])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")