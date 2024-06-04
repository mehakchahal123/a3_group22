from . import db
from datetime import datetime
from flask_login import UserMixin



class User(db.Model, UserMixin):
    # specify table name
    __tablename__ = 'users' 
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    userName = db.Column(db.String(100), index=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, unique=True, nullable=False)
    contactNumber = db.Column(db.String(100))
    password_hash = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))

    bookings = db.relationship('Booking', backref='user')
    # relation to call user.comments and comment.created_by

    comments = db.relationship('Comment', backref='user')
     # string print method
    def __repr__(self):
        return f"Name: {self.name}"


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    eventName = db.Column(db.String(80))
    eventstartDateTime = db.Column(db.DateTime, nullable=False)
    eventendDateTime = db.Column(db.DateTime, nullable=False)
    eventType = db.Column(db.String(50))
    eventLocation = db.Column(db.String(200))
    description = db.Column(db.String(200))
    ticketQuantity = db.Column(db.Integer)
    ticketsAvailable = db.Column(db.Integer)
    ticketPrice = db.Column(db.Float)
    eventImage = db.Column(db.String(400))
    eventStatus = db.Column(db.String(10))

    bookings = db.relationship('Booking', backref='event')
    comments = db.relationship('Comment', backref='event')
     # string print method
    def __repr__(self):
        return f"Name: {self.name}"



class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())

    #add the foreign keys
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    eventid = db.Column(db.Integer, db.ForeignKey('events.id'))
     # string print method
    def __repr__(self):
        return f"Name: {self.comment}"
    
class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    booked_at = db.Column(db.DateTime, default=datetime.now())
    numTickets = db.Column(db.Integer)
    totalPrice = db.Column(db.Float)
    #add the foreign keys
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    eventid = db.Column(db.Integer, db.ForeignKey('events.id'))
    # string print method
    def __repr__(self):
        return f"Name: {self.comment}"