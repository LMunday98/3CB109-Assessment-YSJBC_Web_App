from app import db

class User(db.Model):
    # Always need an id
    id = db.Column(db.Integer, primary_key=True)

    # User attributes
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, email, password):
        self.email = email
        self.password = password

def create_user(new_email, new_password):
    user = User(new_email, new_password)

    # Actually add this user to the database
    db.session.add(user)

    # Save all pending changes to the database
    db.session.commit()

    return user