from app import db
from shutil import copyfile
import datetime, os

class Blog(db.Model):
    __tablename__ = 'blogs'
    __table_args__ = {'extend_existing': True}

    # Always need an id
    id = db.Column(db.Integer, primary_key=True)

    # Blog attributes
    title = db.Column(db.String(128))
    desc = db.Column(db.Text)
    body = db.Column(db.Text)
    thumbnail = db.Column(db.String(128))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, title, desc, body, thumbnail):
        self.title = title
        self.desc = desc
        self.body = body
        self.thumbnail = thumbnail
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    @staticmethod
    def get(id):
        blog = Blog.query.filter_by(id=id).first()
        return blog

    @staticmethod
    def get_all():
        blogs = Blog.query.all()
        return blogs
    
    @classmethod
    def create(cls, title, desc, body, thumbnail='blog1.jpg'):
        blog = Blog(title, desc, body, thumbnail)

        # Actually add user to the database
        db.session.add(blog)

        # Save all pending changes to the database
        db.session.commit()

        return blog

    def update(self, title, desc, body):
        self.title = title
        self.desc = desc
        self.body = body
        self.updated_at = datetime.datetime.now()
        db.session.commit()

    @staticmethod
    def delete(id):
        blog = Blog.query.filter_by(id=id).first()
        db.session.delete(blog)
        db.session.commit()

    @classmethod
    def seed(cls, fake, thumb_id, src, dst):
        title = fake.sentence()
        desc = fake.sentence()
        body = fake.text()
        thumbnail = "blog" + str(thumb_id) + ".jpg"

        copyfile(src+'/'+thumbnail, dst+'/'+thumbnail)
        cls.create(title, desc, body, thumbnail)