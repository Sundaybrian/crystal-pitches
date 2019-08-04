from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    
class User(UserMixin,db.Model):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255),unique=True,index=True)
    bio=db.Column(db.String(255))
    profile_pic_path=db.Column(db.String())
    password_hash=db.Column(db.String())

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)    


    def __repr__(self):
        return f'User {self.username}'


class Posts(db.Model):
    __tablename__='posts'

    id=db.Column(db.Integer,primary_key=True)

    #post_title for the post
    post_title=db.Column(db.String())

    #post_content
    post_content=db.Column(db.String())

    #post_date
    post_date=db.Column(db.DateTime,default=datetime.utcnow())    

    #user id column to link a user to a specific post
    user_id=db.Column(db.Interger,db.ForeignKey('users.id'))

    


class Comment(db.Model):
    __tablename__='comments'

    id=db.Column(db.Integer,primary_key=True)

     #comment a user gives to a post
    comment_content=db.Column(db.String())

    #post id for linking a comment to a specific post
    post_id=db.Column(db.Integer,db.ForeignKey('posts.id'))

    #user id for linking a comment to a specific user
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))



