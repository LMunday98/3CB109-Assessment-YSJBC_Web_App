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
            week_string = new_week + '-1'
            converted_week = datetime.strptime(week_string, "%Y-W%W-%w")
            given_week = get_week(converted_week)
            calendar_week = new_week

        events = Event.query.filter(Event.event_date.between(given_week['Monday'], given_week['Sunday'])).order_by(Event.event_start.asc()).all()
        event_dict = create_event_dict()

        for event in events:
            event_day = event.event_date.strftime("%A")
            dict_day = event_dict[event_day]
            event.event_start = event.event_start.strftime("%H:%M")
            event.event_end = event.event_end.strftime("%H:%M")
            dict_day.append(event)

        week_dict = {}

        # Get month and day number
        for day in given_week:
            converted_date = datetime.strptime(given_week[day], '%Y-%m-%d')
            day_num = converted_date.strftime("%d")
            month = converted_date.strftime("%B")
            week_dict[day] = {'Date' : day_num, 'Month' : month}
            
        url = route + '/training.html'
        return render_template(url, calendar_week=calendar_week, week_dict=week_dict, events=sorted_events, action="Show", msg=msg, msg_colour=msg_colour)
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

            if event_start > event_end:
                return render_template('admin/training.html', action="Create", msg="Please make sure the event start time is earlier the event end!", msg_colour="danger")

            event_type = get_event_type(event_title)
            Event.create(event_title, event_type, event_date, event_start, event_end)
            return redirect('/admin/training')
        else:
            return render_template('admin/training.html', action="Create")
    except Exception as e:
        return(str(e))

def edit(id):
    try:
        event = Event.get(id)
        if event != None:
            return render_template('admin/training.html', action="Edit", event=event)
        else:
            return redirect('/admin/training')
    except Exception as e:
        return(str(e))

def update(method, form_data):
    if method == 'POST':
        try:
            id = form_data['id']
            event_title = form_data['title']
            event_date = form_data['date']
            event_start = form_data['start']
            event_end = form_data['end']

            current_event = Event.get(id)
            if event_start > event_end:
                return render_template('admin/training.html', event=current_event, action="Edit", msg="Please make sure the event start time is earlier the event end!", msg_colour="danger")
            
            event_type = get_event_type(event_title)
            current_event.update(event_title, event_type, event_date, event_start, event_end)
        except Exception as e:
            return(str(e))
    return redirect('/admin/training')

def delete(method, form_data):
    if method == 'POST':
        try:
            delete_id = form_data['delete_id']
            Event.delete(delete_id)
        except Exception as e:
            return(str(e))
    return redirect('/admin/training')

def get_week(given_date):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    monday_date = given_date - timedelta(days = given_date.weekday())
    week_dict = {}

    # Monday -> Sunday
    for day_index in range(0,7):
        new_date = monday_date + timedelta(days=day_index)
        week_dict[days[day_index]] = new_date.strftime('%Y-%m-%d')

    return week_dict

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