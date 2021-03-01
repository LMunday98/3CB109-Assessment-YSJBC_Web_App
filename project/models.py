from app import db
from app.models.user import *
from app.models.blog import *

def migration():
    # Clean migration of db
    print ("Dropping all tables...")
    db.drop_all()
    print ("Done!")
    print ("Creating database tables...")
    db.create_all()
    print ("Done!")

def seed():
    print ("Seeding database...")
    create_user("luke.munday@gmail.com", "LukePass", "Admin")
    create_user("test@gmail.com", "test")
    create_blog("Title", "Desc", "Body")
    print ("Done!")

if __name__ == "__main__":
    migration()
    seed()