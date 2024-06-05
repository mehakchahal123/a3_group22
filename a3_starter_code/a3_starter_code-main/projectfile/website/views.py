from flask import Blueprint, render_template, request, redirect, url_for
from .models import Event, Booking
from . import db
from flask_login import login_required, current_user
mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    events = db.session.scalars(db.select(Event)).all()    
    return render_template('index.html', events=events, selected_category=None)

@mainbp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":
        print(request.args['search'])
        query = "%" + request.args['search'] + "%"
        events = db.session.scalars(db.select(Event).where(Event.eventName.like(query)))
        return render_template('index.html', events=events)
    else:
        return render_template('index.html', events=events)
    
@mainbp.route('/history')
@login_required
def history():
    # Query the database for the current user's bookings
    bookings = Booking.query.filter_by(userid=current_user.id).all()
    return render_template('bhistory.html', bookings=bookings)
