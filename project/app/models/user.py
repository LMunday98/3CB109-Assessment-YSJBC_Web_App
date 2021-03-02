from app import db
from app import bcrypt

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    # Always need an id
    id = db.Column(db.Integer, primary_key=True)

    # User attributes
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    account_type = db.Column(db.String(8), unique=False, default="User")

    def __init__(self, email, password, account_type):
        self.email = email
        self.password_hash = self.hash_password(password)
        self.account_type = account_type

    @staticmethod
    def hash_password(password):
        return bcrypt.generate_password_hash(password)

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

    @classmethod
    def seed(cls, fake):
        email = fake.email()
        cls.create_user(email, email)