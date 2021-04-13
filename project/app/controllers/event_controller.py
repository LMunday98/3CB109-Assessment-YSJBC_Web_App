from app.models.event import *
from flask import render_template, redirect, request
import datetime
from datetime import datetime, timedelta

def show(route, method, form_data):
    try:
        given_week = get_week(datetime.now())

        if method == 'POST':
            new_week = form_data['week']
            converted_week = datetime.strptime(new_week + '-1', '%G-W%V-%u')
            given_week = get_week(converted_week)

        events = Event.query.filter(Event.event_start.between(given_week['Monday'], given_week['Sunday']))
        event_dict = create_event_dict()

        for event in events:
            event_day = event.event_start.strftime("%A")
            dict_day = event_dict[event_day]
            dict_day.append(event)

        print(event_dict)

        url = route + '/training.html'
        return render_template(url, events=events)
    except Exception as e:
        return(str(e))

def get_week(given_date):
    monday_date = given_date - timedelta(days = given_date.weekday())
    sunday_date = monday_date + timedelta(days=7)
    return {'Monday' : monday_date.strftime('%Y-%m-%d'), 'Sunday' : sunday_date.strftime('%Y-%m-%d')}

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