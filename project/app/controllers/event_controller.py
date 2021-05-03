from app.models.event import *
from flask import render_template, redirect, request
from datetime import date, time, datetime, timedelta

def show(route, method, form_data, msg="", msg_colour=""):
    try:
        today = date.today()
        given_week = get_week(today)
        calendar_week = today.strftime('%Y-W%W')

        if method == 'POST':
            new_week = form_data['week']
            converted_week = datetime.strptime(new_week + '-1', '%G-W%V-%u')
            given_week = get_week(converted_week)
            calendar_week = new_week

        events = Event.query.filter(Event.event_date.between(given_week['Monday'], given_week['Sunday'])).all()
        event_dict = create_event_dict()

        for event in events:
            event_day = event.event_date.strftime("%A")
            dict_day = event_dict[event_day]
            event.event_start = event.event_start.strftime("%H:%M")
            event.event_end = event.event_end.strftime("%H:%M")
            dict_day.append(event)

        url = route + '/training.html'
        return render_template(url, calendar_week=calendar_week, events=event_dict, action="Show", msg=msg, msg_colour=msg_colour)
    except Exception as e:
        return(str(e))

def create(method, form_data):
    try:
        if method == 'POST':
            event_title = form_data['title']
            event_date = form_data['date']
            event_start = form_data['start']
            event_end = form_data['end']

            if event_title == 'Default':
                return render_template('admin/training.html', action="Create", msg="Please select an event type", msg_colour="danger")

            event_type = get_event_type(event_title)
            Event.create(event_title, event_type, event_date, event_start, event_end)
            return redirect('/admin/training')
        else:
            return render_template('admin/training.html', action="Create")
    except Exception as e:
        return(str(e))

def edit(id):
    try:
        ex=1
    except Exception as e:
        return(str(e))

def delete(method, form_data):
    if method == 'POST':
        try:
            delete_id = form_data['delete_id']
            Event.delete(delete_id)
        except Exception as e:
            return(str(e))
    return redirect('/admin/training')

def get_week(given_date):
    monday_date = given_date - timedelta(days = given_date.weekday())
    sunday_date = monday_date + timedelta(days=6)
    return {'Monday' : monday_date.strftime('%Y-%m-%d'), 'Sunday' : sunday_date.strftime('%Y-%m-%d')}

def get_event_type(event_title):
    type_dict = {
        'Water Session' : 'event-blue',
        'Erg' : 'event-orange',
        'Weight Training' : 'event-purple',
        'Yoga' : 'event-green'
    }
    return type_dict[event_title]

def create_event_dict():
    event_dict = {
        'Monday' : [],
        'Tuesday' : [],
        'Wednesday' : [],
        'Thursday' : [],
        'Friday' : [],
        'Saturday' : [],
        'Sunday' : [],
    }
    return event_dict