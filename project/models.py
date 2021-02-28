from app import db
from app.models.user import *
from app.models.dessert import *

if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print ("Creating database tables...")
    db.create_all()
    print ("Done!")