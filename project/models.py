from app import db
from app.models.user import *

def migration():
    # Clean migration of db
    print ("Dropping all tables...")
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print ("Drop table %s" % table)
        db.session.execute(table.delete())
    db.session.commit()
    print ("Creating database tables...")
    db.create_all()
    print ("Done!")

def seed():
    print ("Seeding database...")
    create_user("luke.munday@gmail.com", "LukePass")
    print ("Done!")

if __name__ == "__main__":
    migration()
    seed()