from app import db,login_manager
from datetime import datetime
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    original_password = db.Column(db.String(255),nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
        self.original_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.original_password,password) 
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f'User {self.username}'

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    post = db.Column(db.Text(), nullable = False)
    comment = db.relationship('Comment',backref='post',lazy='dynamic')
    upvote = db.relationship('Upvote',backref='post',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='post',lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    time = db.Column(db.DateTime, default = datetime.utcnow)
    category = db.Column(db.String(255), index = True,nullable = False)
    
    def save_post(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

        
    def __repr__(self):
        return f'Post {self.post}'

