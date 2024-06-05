from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Event, Comment, Booking
from .forms import EventForm, CommentForm, BookingForm, EditForm
from . import db
import os
from werkzeug.utils import secure_filename
#additional import:
from flask_login import login_required, current_user

eventbp = Blueprint('event', __name__, url_prefix='/events')

@eventbp.route('/<id>')
def show(id):
    event = db.session.scalar(db.select(Event).where(Event.id==id))
    # create the comment form
    form = CommentForm()
    bookingform = BookingForm()
    #events = [event]
    return render_template('events/show.html', event=event, form=form, bookingform=bookingform)


@eventbp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
  #print('Method type: ', request.method)
  form = EventForm()
  if form.validate_on_submit():
    #call the function that checks and returns image
    db_file_path = check_upload_file(form)
    event = Event(userid=current_user.id,eventName=form.eventName.data,description=form.description.data, eventstartDateTime=form.eventstartDateTime.data, eventendDateTime=form.eventendDateTime.data, eventType=form.eventType.data, eventLocation=form.eventLocation.data, ticketQuantity=form.ticketQuantity.data, ticketsAvailable=form.ticketQuantity.data, ticketPrice=form.ticketPrice.data,
    eventImage=db_file_path,eventStatus='Open')
    # add the object to the db session
    db.session.add(event)
    # commit to the database
    db.session.commit()
    flash('Successfully created new event', 'success')
    #Always end with redirect when form is valid
    return redirect(url_for('event.create'))
  return render_template('events/create.html', form=form)

@eventbp.route('/edit/<int:eventid>', methods=['GET', 'POST'])
@login_required
def edit_event(eventid):
    event = Event.query.get_or_404(eventid)
    if current_user.id != event.userid:
        flash('You do not have permission to edit this event.', 'danger')
        return redirect(url_for('event.show', id=event.id))  
    form = EditForm(obj=event)  # Pre-fill form with event data on GET

    if form.validate_on_submit():
        # Update the event details
        event.eventName=form.eventName.data
        event.description=form.description.data
        event.eventstartDateTime=form.eventstartDateTime.data
        event.eventendDateTime=form.eventendDateTime.data
        event.eventType=form.eventType.data
        event.eventLocation=form.eventLocation.data
        event.ticketQuantity=form.ticketQuantity.data
        event.ticketsAvailable=form.ticketQuantity.data
        event.ticketPrice=form.ticketPrice.data
        event.status = form.status.data

        db.session.commit()
        flash('Event updated successfully!', 'success')
        return redirect(url_for('event.show', id=event.id))  

    return render_template('events/edit.html', form=form, eventid=eventid)

@eventbp.route('/category/<category>')
def filter_by_category(category):
    events = db.session.query(Event).filter(Event.eventType == category).all()
    return render_template('index.html', events=events, selected_category=category)

def check_upload_file(form):
  #get file data from form  
  fp = form.eventImage.data
  filename = fp.filename
  #get the current path of the module file… store image file relative to this path  
  BASE_PATH = os.path.dirname(__file__)
  #upload file location – directory of this file/static/image
  upload_path = os.path.join(BASE_PATH, 'static/img', secure_filename(filename))
  #store relative path in DB as image location in HTML is relative
  db_upload_path = '/static/img/' + secure_filename(filename)
  #save the file and return the db upload path
  fp.save(upload_path)
  return db_upload_path

@eventbp.route('/<id>/comment', methods=['GET', 'POST'])  
@login_required
def comment(id):  
    form = CommentForm()
    #get the destination object associated to the page and the comment
    event = db.session.scalar(db.select(Event).where(Event.id==id))
    if form.validate_on_submit():  
      #read the comment from the form
      comment = Comment(comment=form.text.data, event=event,
                        user=current_user) 
      #here the back-referencing works - comment.destination is set
      # and the link is created
      db.session.add(comment) 
      db.session.commit() 
      #flashing a message which needs to be handled by the html
      flash('Your comment has been added', 'success')  
      # print('Your comment has been added', 'success') 
    # using redirect sends a GET request to destination.show
    return redirect(url_for('event.show', id=id))

@eventbp.route('<int:eventid>/booking', methods=['POST'])
@login_required
def book(eventid):
    form = BookingForm()
    event = db.session.scalar(db.select(Event).where(Event.id==eventid))
    if form.validate_on_submit():  
      # Pulling ticket data and storing in field tickets_to_book
      tickets_to_book = form.numtickets.data
      # Verifying the number of tickets remaining
      tickets_remaining = event.ticketsAvailable
      # Checking that remaining tickets is greater than number of tickets remaining
      if tickets_to_book > tickets_remaining:
         flash(f'Not enough tickets available. Only {tickets_remaining} tickets left.', 'danger')
         return redirect(url_for('event.show', id=eventid))
      # read the booking from the form
      booking = Booking(numTickets=form.numtickets.data, totalPrice=(form.numtickets.data*event.ticketPrice), booked_at=datetime.now(), event=event, user=current_user) 
      db.session.add(booking) 
      event.ticketsAvailable = event.ticketsAvailable - tickets_to_book
      db.session.commit() 
      # Update the event status if no tickets are remaining
      if event.ticketsAvailable == 0:
        event.status = "Sold Out"
        db.session.commit()
      # flashing a message which needs to be handled by the html
      flash('Your booking has been added', 'success')  
    #Error handling in case booking fails for unknown reason
    else:
       flash('Failed to book tickets.', 'danger')
    # using redirect sends a GET request to destination.show
    return redirect(url_for('event.show', id=eventid))

