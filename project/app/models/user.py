from app import db
from app import bcrypt

class User(db.Model):
    # Always need an id
    id = db.Column(db.Integer, primary_key=True)

    # User attributes
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    account_type = db.Column(db.String(8), unique=False, default="User")

    def __init__(self, email, password, account_type):
        self.email = email
        self.set_password(password)
        self.account_type = account_type

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def create_user(new_email, new_password, account_type="User"):
        user = User(new_email, new_password, account_type)

        # Actually add user to the database
        db.session.add(user)

        # Save all pending changes to the database
        db.session.commit()

        return user

    def get_user(email):
        user = User.query.filter_by(email=email).first()
        return user

