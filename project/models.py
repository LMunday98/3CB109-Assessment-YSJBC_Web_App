from app import db
from app.models import *
from faker import Faker
from datetime import date, time, datetime, timedelta
import os, shutil

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
        # Seed users
        User.create("luke@admin", "LukePass", "admin")
        User.create("mike@admin", "Mike", "admin")
        User.create("user@gmail.com", "user", "user")
        User.create("guest@gmail.com", "guest")
        fake = Faker()
        for _ in range(5):
            User.seed(fake, 'user')
        for _ in range(5):
            User.seed(fake)

        # Seed blogs
        dir_path = os.path.dirname(os.path.realpath(__file__))
        static_path = dir_path + '/app/static/'
        src_thumb_path = static_path + 'seed_thumbnails'
        dst_thumb_path = static_path + 'blog_thumbnails'

        access_rights = 0o755

        try:
            shutil.rmtree(dst_thumb_path)
        except Exception as e:
            print(e)

        try:
            os.mkdir(dst_thumb_path, access_rights)
        except Exception as e:
            print(e)

        for _ in range(4):
            Blog.seed(fake,_+1,src_thumb_path,dst_thumb_path)

        # Seed events
        week_dates = get_week(date.today())
        # Monday
        Event.create("Water Session", "event-blue", week_dates['Monday'], time(9, 30), time(10, 30))
        Event.create("Erg", "event-orange", week_dates['Monday'], time(11, 30), time(13, 45))
        Event.create("Yoga", "event-green", week_dates['Monday'], time(14, 00), time(15, 00))
        # Tuesday
        Event.create("Weight Training", "event-purple", week_dates['Tuesday'],  time(12, 30), time(14, 0))
        Event.create("Yoga", "event-green", week_dates['Tuesday'],  time(14, 30), time(15, 30))
        # Wednesday
        Event.create("Water Session", "event-blue", week_dates['Wednesday'],  time(9, 30), time(12, 30))
        Event.create("Water Session", "event-blue", week_dates['Wednesday'],  time(13, 30), time(16, 30))
        # Thursday
        Event.create("Erg", "event-orange", week_dates['Thursday'],  time(15, 30), time(16, 30))
        Event.create("Yoga", "event-green", week_dates['Thursday'],  time(17, 30), time(18, 30))
        # Friday
        Event.create("Water Session", "event-blue", week_dates['Friday'],  time(9, 30), time(10, 30))
        # Saturday
        # Empty day
        # Sunday
        Event.create("Weight Training", "event-purple", week_dates['Sunday'],  time(18, 30), time(20, 00))
        return "Done!"
    except Exception as e:
        return(str(e))

def get_week(given_date):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    monday_date = given_date - timedelta(days = given_date.weekday())
    week_dict = {}

    # Monday -> Sunday
    for day_index in range(0,7):
        new_date = monday_date + timedelta(days=day_index)
        week_dict[days[day_index]] = new_date.strftime('%Y-%m-%d')

    return week_dict

if __name__ == "__main__":
    print(migrate())
    print(seed())