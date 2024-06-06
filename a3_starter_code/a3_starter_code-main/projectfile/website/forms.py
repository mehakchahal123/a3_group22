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
  submit = SubmitField('Post')

#Create new events
class EventForm(FlaskForm): 
  eventName = StringField('Event Name', validators=[InputRequired(), Length(max=80)]) 
  eventstartDateTime = DateTimeLocalField('Start Date and Time', validators=[InputRequired()]) 
  eventendDateTime = DateTimeLocalField('End Date and Time', validators=[InputRequired()]) 
  eventLocation = StringField('Event Location', validators=[InputRequired(), Length(max=200)]) 
  description = TextAreaField('Description', validators=[InputRequired(), Length(max=500)]) 
  ticketQuantity = IntegerField('Ticket Quantity', validators=[InputRequired(), NumberRange(min=1)]) 
  ticketPrice = IntegerField('Ticket Price', validators=[InputRequired(), NumberRange(min=0)]) 
  eventImage = FileField('Event Image', validators=[ FileRequired(message='Image cannot be empty'), FileAllowed(ALLOWED_FILE, message='Only supports PNG, ]PG, png, jpg')])
  #eventStatus = SelectField('Event Status', choices=[('Open', 'Open'), ('Inactive', 'Inactive'), ('Cancelled', 'Cancelled'), ('Sold Out', 'Sold Out')], validators=[InputRequired()]) 
  eventType = SelectField('Event Category', choices=[('Illusion', 'Illusion'), ('Comedy', 'Comedy'), ('Levitation', 'Levitation'), ('Transformation', 'Transformation'), ('Mentalism', 'Mentalism'), ('Penetration', 'Penetration')], validators=[InputRequired()]) 
  submit = SubmitField("Create Event")


class EditForm(FlaskForm):
    eventName = StringField('Event Name', validators=[InputRequired(), Length(max=80)])
    eventstartDateTime = DateTimeLocalField('Start Date and Time', validators=[InputRequired()]) 
    eventendDateTime = DateTimeLocalField('End Date and Time', validators=[InputRequired()]) 
    eventLocation = StringField('Event Location', validators=[InputRequired(), Length(max=200)]) 
    description = TextAreaField('Description', validators=[InputRequired(), Length(max=500)]) 
    ticketQuantity = IntegerField('Ticket Quantity', validators=[InputRequired(), NumberRange(min=1)]) 
    ticketPrice = IntegerField('Ticket Price', validators=[InputRequired(), NumberRange(min=0)]) 
    #eventImage = FileField('Event Image', validators=[ FileRequired(message='Image cannot be empty'), FileAllowed(ALLOWED_FILE, message='Only supports PNG, ]PG, png, jpg')])
    eventType = SelectField('Event Category', choices=[('Illusion', 'Illusion'), ('Comedy', 'Comedy'), ('Levitation', 'Levitation'), ('Transformation', 'Transformation'), ('Mentalism', 'Mentalism'), ('Penetration', 'Penetration')], validators=[InputRequired()])  
    eventStatus = SelectField(' Event Status', choices=[('Open', 'Open'), ('Cancelled', 'Cancelled'), ('Sold Out', 'Sold Out'),('Inactive', 'Inactive')], validators=[InputRequired()]) 
    submit = SubmitField('Update Event')



class BookingForm(FlaskForm):
   numtickets = IntegerField('Number of Tickets', validators=[InputRequired(), NumberRange(min=1, max=10)])
   create = SubmitField('Book')