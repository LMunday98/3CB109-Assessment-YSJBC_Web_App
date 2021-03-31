from app import db
from app import bcrypt
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    # Always need an id
    id = db.Column(db.Integer, primary_key=True)

    # User attributes
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    account_type = db.Column(db.String(8), unique=False, default="guest")
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, email, password, account_type):
        self.email = email
        self.password_hash = self.hash_password(password)
        self.account_type = account_type

    @staticmethod
    def hash_password(password):
        return bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def check_verified(self):
        if self.account_type == 'guest':
            return False
        else:
            return True

    @classmethod
    def create(cls, new_email, new_password, account_type="guest"):
        user = User(new_email, new_password, account_type)

        # Actually add user to the database
        db.session.add(user)

        # Save all pending changes to the database
        db.session.commit()

        return user

    @staticmethod
    def get(email):
        user = User.query.filter_by(email=email).first()
        return user

    @classmethod
    def seed(cls, fake):
        email = fake.email()
        cls.create(email, email)

    def is_active(self):
        """True, as all users are active."""
        return True

    @staticmethod
    def get_user_by_id(id):
        """Return the email address to satisfy Flask-Login's requirements."""
        user = User.query.filter_by(id=id).first()
        return user

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False