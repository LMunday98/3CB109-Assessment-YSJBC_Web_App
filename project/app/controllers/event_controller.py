from app.models.event import *
from flask import render_template, redirect, request
import datetime
from datetime import datetime, timedelta

def show(route):
    try:
        now = datetime.now()
        monday_date = now - timedelta(days = now.weekday())
        sunday_date = monday_date + timedelta(days=7)

        monday_str = monday_date.strftime('%Y-%m-%d')
        sunday_str = sunday_date.strftime('%Y-%m-%d')

        events = Event.query.filter(Event.event_start.between(monday_str, sunday_str))
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