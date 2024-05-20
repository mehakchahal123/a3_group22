from . import db
from datetime import datetime
from flask_login import UserMixin



class User(db.Model, UserMixin):
    # specify table name
    __tablename__='users' 
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    userName = db.Column(db.String(100), index=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, unique=True, nullable=False)
    contactNumber = db.Column(db.String(100))
    password_hash = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    user = db.relationship('Order', backref='user')
    # relation to call user.comments and comment.created_by

    comments = db.relationship('Comment', backref='user')
     # string print method
    def __repr__(self):
        return f"Name: {self.name}"


class Event(db.model):
    __tablename__ = 'event'
    eventid = db.Column(db.Integer, primary_key=True, nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    eventName = db.Column(db.String(80))
    eventstartDate = db.Column(db.Date, nullable=False)
    eventstartTime = db.Column(db.Time, nullable=False)
    eventendDate = db.Column(db.Date, nullable=False)
    eventendTime = db.Column(db.Time, nullable=False)
    eventType = db.Column(db.Integer, db.ForeignKey('type.typeid'))
    eventStates = db.Column(db.Integer, db.ForeignKey('states.statesid'))
    eventLocation = db.Column(db.String(200))
    description = db.Column(db.String(200))
    ticketQuantity = db.Column(db.Integer)
    ticketsAvailable = db.Column(db.Integer)
    ticketPrice = db.Column(db.Integer)
    eventImage = db.Column(db.String(400))

    order = db.relationship('Order', backref='event')
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
    eventid = db.Column(db.Integer, db.ForeignKey('event.eventid'))
     # string print method
    def __repr__(self):
        return f"Name: {self.name}"