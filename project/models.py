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
        Event.create("Rowing Water Session", "rowing", datetime(2021, 4, 11, 9, 30, 0, 0), datetime(2021, 4, 11, 10, 30, 0, 0))

        Event.create("Rowing Water Session", "rowing", datetime(2021, 4, 12, 9, 30, 0, 0), datetime(2021, 4, 12, 10, 30, 0, 0))
        Event.create("Rowing Water Session", "rowing", datetime(2021, 4, 13, 9, 30, 0, 0), datetime(2021, 4, 13, 10, 30, 0, 0))
        Event.create("Rowing Water Session", "rowing", datetime(2021, 4, 14, 9, 30, 0, 0), datetime(2021, 4, 14, 10, 30, 0, 0))
        Event.create("Rowing Water Session", "rowing", datetime(2021, 4, 15, 9, 30, 0, 0), datetime(2021, 4, 15, 10, 30, 0, 0))
        Event.create("Rowing Water Session", "rowing", datetime(2021, 4, 16, 9, 30, 0, 0), datetime(2021, 4, 16, 10, 30, 0, 0))
        Event.create("Rowing Water Session", "rowing", datetime(2021, 4, 17, 9, 30, 0, 0), datetime(2021, 4, 17, 10, 30, 0, 0))
        Event.create("Rowing Water Session", "rowing", datetime(2021, 4, 18, 9, 30, 0, 0), datetime(2021, 4, 18, 10, 30, 0, 0))
        
        Event.create("Rowing Water Session", "rowing", datetime(2021, 4, 19, 9, 30, 0, 0), datetime(2021, 4, 19, 10, 30, 0, 0))
        return "Done!"
    except Exception as e:
        return(str(e))

if __name__ == "__main__":
    print(migrate())
    print(seed())