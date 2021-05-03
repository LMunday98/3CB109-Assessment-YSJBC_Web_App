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

        blog1 = {'title' : 'Walk all over cancer!',
        'desc' : 'Amazing work by everyone taking part in our charity fundraiser!',
        'body' : 'This March York St John Boat Club are walking 10,000 steps a day throughout the month to help beat cancer sooner. Help us Walk All Over Cancer and fund life-saving research by sponsoring us. Cancer survival rates have doubled over the past 40 years. Consistent progress is being made but improvements to technology and ground-breaking work offer new opportunities to find different ways to prevent, diagnose and treat cancer and improve survival rates even further. Help Cancer Research UK improve results even faster.',
        'datetime' : datetime(2021, 3, 27, 15, 45)}

        blog2 = {'title' : 'This Girl Can week!',
        'desc' : 'A big shout out to all the members that took part!',
        'body' : 'It’s This Girl Can week and what can Girls do? ROW! This morning a wonderful turn out saw lots of female members pushing themselves on ergs and leg/abs based exercises! YOU GO GIRLS!!',
        'datetime' : datetime(2021, 4, 5, 17, 1)}

        blog3 = {'title' : 'Club AGM',
        'desc' : 'The new 2021/2022 boat club committee!',
        'body' : "Congratulations to the new club exec! We're sure you'll all do an amazing job in the new year and a big thank you to everyone who participated and voted!",
        'datetime' : datetime(2021, 5, 12, 11, 27)}

        blog4 = {'title' : 'Big win for YSJ!',
        'desc' : 'YSJBC smash head of the river competition!',
        'body' : 'Today was a big day for the boat club, as we take home the win at the annual competition between York University Boat Club, York City Boat Club and ourselves!',
        'datetime' : datetime(2021, 5, 19, 9, 55)}

        population_data = [blog1, blog2, blog3, blog4]

        for blog_index in range(4):
            Blog.seed(population_data[blog_index], blog_index + 1, src_thumb_path, dst_thumb_path)

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