from app.models.event import *
from flask import render_template, redirect, request
import datetime

def show(route):
    try:
        url = route + '/training.html'
        events = Event.query.order_by(Event.updated_at.desc()).all()

        event_dict = create_event_dict()

        for event in events:
            event_day = event.event_start.strftime("%A")
            dict_day = event_dict[event_day]
            dict_day.append(event)

        print(event_dict)

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