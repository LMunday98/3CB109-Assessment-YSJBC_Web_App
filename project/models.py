from app import db
from app.models import *
from faker import Faker

def migration():
    # Clean migration of db
    print ("Dropping all tables...")
    db.drop_all()
    print ("Done!")
    print ("Creating database tables...")
    db.create_all()
    print ("Done!")

def seed():
    print ("Seeding tables...")
    User.create_user("luke.munday@gmail.com", "LukePass", "Admin")
    User.create_user("test@gmail.com", "test")

    fake = Faker()
    for _ in range(10):
        User.seed(fake)

    for _ in range(6):
        Blog.seed(fake)

    print ("Done!")

if __name__ == "__main__":
    migration()
    seed()