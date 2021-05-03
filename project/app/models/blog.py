from app import db
from shutil import copyfile
import datetime

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

    def __init__(self, title, desc, body, thumbnail, created_at, updated_at):
        self.title = title
        self.desc = desc
        self.body = body
        self.thumbnail = thumbnail
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def get(id):
        blog = Blog.query.filter_by(id=id).first()
        return blog

    @staticmethod
    def get_all():
        blogs = Blog.query.all()
        return blogs
    
    @classmethod
    def create(cls, title, desc, body, thumbnail='blog1.jpg', created_at=datetime.datetime.now(), updated_at=datetime.datetime.now()):
        blog = Blog(title, desc, body, thumbnail, created_at, updated_at)

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
    def seed(cls, population_data, thumb_id, src, dst):
        title = population_data['title']
        desc = population_data['desc']
        body = population_data['body']
        given_datetime = population_data['datetime']
        thumbnail = "blog" + str(thumb_id) + ".jpg"

        copyfile(src + '/' + thumbnail, dst + '/' + thumbnail)
        cls.create(title, desc, body, thumbnail, given_datetime ,given_datetime)