from app.models.event import *
from flask import render_template, redirect, request
from datetime import date, time, datetime, timedelta

def show(route, method, form_data, msg="", msg_colour=""):
    try:
        # Get todays date
        # Get yyyy-mm-dd of each day in given week
        # Get yyyy-ww from todays date
        today = date.today()
        given_week = get_week(today)
        calendar_week = today.strftime('%Y-W%W')

        if method == 'POST':
            # get form data
            new_week = form_data['week']
            # instead of getting the week from today, use the week specified from the user
            week_string = new_week + '-1'
            # convert from yyyy-ww to yyyy-ww-1
            # then from yyyy-ww-1 to yyyy-mm-dd
            # Get yyyy-mm-dd of each day in given week
            converted_week = datetime.strptime(week_string, "%Y-W%W-%w")
            given_week = get_week(converted_week)
            calendar_week = new_week

        # search for all events between the monday and sunday of the specified dates
        events = Event.query.filter(Event.event_date.between(given_week['Monday'], given_week['Sunday'])).order_by(Event.event_start.asc()).all()
        # create a dict, ready to populate with the events
        event_dict = create_event_dict()

        # for each event found between the specified dates, format the date, start time and end time into end formats
        for event in events:
            event_day = event.event_date.strftime("%A")
            dict_day = event_dict[event_day]
            event.event_start = event.event_start.strftime("%H:%M")
            event.event_end = event.event_end.strftime("%H:%M")
            dict_day.append(event)

        week_dict = {}

        # Get month and day number for each day in the given week
        # Eg: 4 May from 2021-05-04
        for day in given_week:
            converted_date = datetime.strptime(given_week[day], '%Y-%m-%d')
            day_num = converted_date.strftime("%d")
            month = converted_date.strftime("%B")
            week_dict[day] = {'Date' : day_num, 'Month' : month}
            
        # gen route dependin on user level of permissions
        url = route + '/training.html'
        return render_template(url, calendar_week=calendar_week, week_dict=week_dict, events=event_dict, action="Show", msg=msg, msg_colour=msg_colour)
    except Exception as e:
        return(str(e))

def create(method, form_data):
    try:
        if method == 'POST':
            # Get form data
            event_title = form_data['title']
            event_date = form_data['date']
            event_start = form_data['start']
            event_end = form_data['end']

            # If user didnt select an event type, reset form and send message
            if event_title == 'Default':
                return render_template('admin/training.html', action="Create", msg="Please select an event type", msg_colour="danger")

            # check the start and end times are correct
            if event_start > event_end:
                return render_template('admin/training.html', action="Create", msg="Please make sure the event start time is earlier the event end!", msg_colour="danger")

            # get event type from title
            event_type = get_event_type(event_title)
            Event.create(event_title, event_type, event_date, event_start, event_end)
            return redirect('/admin/training')
        else:
            return render_template('admin/training.html', action="Create")
    except Exception as e:
        return(str(e))

def edit(id):
    try:
        # Check event id in url and then load the edit form
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
            # get form data
            id = form_data['id']
            event_title = form_data['title']
            event_date = form_data['date']
            event_start = form_data['start']
            event_end = form_data['end']

            # get event from id
            current_event = Event.get(id)
            if event_start > event_end:
                return render_template('admin/training.html', event=current_event, action="Edit", msg="Please make sure the event start time is earlier the event end!", msg_colour="danger")
            
            # update event data
            event_type = get_event_type(event_title)
            current_event.update(event_title, event_type, event_date, event_start, event_end)
        except Exception as e:
            return(str(e))
    return redirect('/admin/training')

def delete(method, form_data):
    if method == 'POST':
        try:
            # get form data
            # delete event from id
            delete_id = form_data['delete_id']
            Event.delete(delete_id)
        except Exception as e:
            return(str(e))
    return redirect('/admin/training')

def get_week(given_date):
    # calc the monday date of the day / week specified
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    monday_date = given_date - timedelta(days = given_date.weekday())
    week_dict = {}

    # get the yyyy-mm-dd of Monday -> Sunday
    for day_index in range(0,7):
        new_date = monday_date + timedelta(days=day_index)
        week_dict[days[day_index]] = new_date.strftime('%Y-%m-%d')

    return week_dict

def get_event_type(event_title):
    # convert event title into event type, used to apply css classes
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