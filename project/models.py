from app import db
from app.models import *
from faker import Faker
from datetime import datetime

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
        # Monday
        Event.create("Water Session", "event-1")
        #Event.create("Water Session", "event-1", datetime(2021, 4, 12, 9, 30), datetime(2021, 4, 12, 10, 30))
        #Event.create("Erg", "event-2", datetime(2021, 4, 12, 11, 30), datetime(2021, 4, 12, 13, 45))
        #Event.create("Yoga", "event-4", datetime(2021, 4, 12, 14, 00), datetime(2021, 4, 12, 15, 00))
        # Tuesday
        #Event.create("Weight Training", "event-3", datetime(2021, 4, 13, 12, 30), datetime(2021, 4, 13, 14, 0))
        #Event.create("Yoga", "event-4", datetime(2021, 4, 13, 14, 30), datetime(2021, 4, 13, 15, 30))
        # Wednesday
        #Event.create("Water Session", "event-1", datetime(2021, 4, 14, 9, 30), datetime(2021, 4, 14, 12, 30))
        #Event.create("Water Session", "event-1", datetime(2021, 4, 14, 13, 30), datetime(2021, 4, 14, 16, 30))
        # Thursday
        #Event.create("Erg", "event-2", datetime(2021, 4, 15, 15, 30), datetime(2021, 4, 15, 16, 30))
        #Event.create("Yoga", "event-4", datetime(2021, 4, 15, 17, 30), datetime(2021, 4, 15, 18, 30))
        # Friday
        #Event.create("Water Session", "event-1", datetime(2021, 4, 16, 9, 30), datetime(2021, 4, 16, 10, 30))
        # Monday
        #Event.create("Water Session", "event-1", datetime(2021, 4, 19, 9, 30), datetime(2021, 4, 19, 10, 30))
        return "Done!"
    except Exception as e:
        return(str(e))

if __name__ == "__main__":
    print(migrate())
    print(seed())