from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, DateTimeLocalField, IntegerField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo, NumberRange
from flask_wtf.file import FileRequired, FileField, FileAllowed

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

ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}

#User comment
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')

#Create new destination
class EventForm(FlaskForm): 
  eventName = StringField('Event Name', validators=[InputRequired(), Length(max=80)]) 
  eventstartDateTime = DateTimeLocalField('Start Date and Time', validators=[InputRequired()], format='%Y4m4d %H:%m:%S') 
  eventendDateTime = DateTimeLocalField('End Date and Time', validators=[InputRequired()], format='%Y4m4d %H:%M:%S') 
  eventType = StringField('Event Type', validators=[InputRequired(), Length(max=50)]) 
  eventLocation = StringField('Event Location', validators=[InputRequired(), Length(max=200)]) 
  description = TextAreaField('Description', validators=[InputRequired(), Length(max=500)]) 
  ticketQuantity = IntegerField('Ticket Quantity', validators=[InputRequired(), NumberRange(min=1)]) 
  ticketPrice = IntegerField('Ticket Price', validators=[InputRequired(), NumberRange(min=0)]) 
  eventImage = FileField('Event Image', validators=[ FileRequired(message='Image cannot be empty'), FileAllowed(ALLOWED_FILE, message='Only supports PNG, ]PG, png, jpg')])
  eventStatus = SelectField('Event Status', choices=[('Open', 'Open'), ('Inactive', 'Inactive'), ('Cancelled', 'Cancelled'), ('Sold Out', 'Sold Out')], validators=[InputRequired()]) 
  eventType = SelectField('Event Status', choices=[('Cat1', 'Cat1'), ('Cat2', 'Cat2'), ('Cat3', 'Cat3'), ('Cato', 'Cat 5')], validators=[InputRequired()]) 
  submit = SubmitField("Create Event") 

