from app import db
from app.models import *
from faker import Faker

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
        User.create("luke.munday@gmail.com", "LukePass", "admin")
        User.create("test@gmail.com", "test")
        fake = Faker()
        for _ in range(10):
            User.seed(fake)
        for _ in range(6):
            Blog.seed(fake)
        return "Done!"
    except Exception as e:
        return(str(e))

if __name__ == "__main__":
    print(migrate())
    print(seed())