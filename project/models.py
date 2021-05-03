from app import db
from app.models import *
from faker import Faker
import datetime

def migrate():
    print ("Migrating database...")
    try:
        db.drop_all()
        db.create_all()
        return "Done!"
    except Exception as e:
        return(str(e))

def seed():
    print ("Seeding tables...")
    try:
        User.create("luke@admin", "LukePass", "admin")
        User.create("mike@admin", "Mike", "admin")
        User.create("user@gmail.com", "user", "user")
        User.create("guest@gmail.com", "guest")
        fake = Faker()
        for _ in range(5):
            User.seed(fake, 'user')
        for _ in range(5):
            User.seed(fake)
        for _ in range(12):
            Blog.seed(fake,_+1)
        # Sunday
        Event.create("Water Session", "event-blue", datetime.date(2021, 4, 11), datetime.time(9, 30), datetime.time(10, 30))
        # Monday
        Event.create("Water Session", "event-blue", datetime.date(2021, 4, 12), datetime.time(9, 30), datetime.time(10, 30))
        Event.create("Erg", "event-orange", datetime.date(2021, 4, 12), datetime.time(11, 30), datetime.time(13, 45))
        Event.create("Yoga", "event-green", datetime.date(2021, 4, 12), datetime.time(14, 00), datetime.time(15, 00))
        # Tuesday
        Event.create("Weight Training", "event-purple", datetime.date(2021, 4, 13),  datetime.time(12, 30), datetime.time(14, 0))
        Event.create("Yoga", "event-green", datetime.date(2021, 4, 13),  datetime.time(14, 30), datetime.time(15, 30))
        # Wednesday
        Event.create("Water Session", "event-blue", datetime.date(2021, 4, 14),  datetime.time(9, 30), datetime.time(12, 30))
        Event.create("Water Session", "event-blue", datetime.date(2021, 4, 14),  datetime.time(13, 30), datetime.time(16, 30))
        # Thursday
        Event.create("Erg", "event-orange", datetime.date(2021, 4, 15),  datetime.time(15, 30), datetime.time(16, 30))
        Event.create("Yoga", "event-green", datetime.date(2021, 4, 15),  datetime.time(17, 30), datetime.time(18, 30))
        # Friday
        Event.create("Water Session", "event-blue", datetime.date(2021, 4, 16),  datetime.time(9, 30), datetime.time(10, 30))
        # Saturday
        Event.create("Water Session", "event-blue", datetime.date(2021, 4, 17),  datetime.time(9, 30), datetime.time(10, 30))
        # Sunday
        Event.create("Water Session", "event-blue", datetime.date(2021, 4, 18),  datetime.time(9, 30), datetime.time(10, 30))
        # Monday
        Event.create("Water Session", "event-blue", datetime.date(2021, 4, 19),  datetime.time(9, 30), datetime.time(10, 30))
        return "Done!"
    except Exception as e:
        return(str(e))

if __name__ == "__main__":
    print(migrate())
    print(seed())