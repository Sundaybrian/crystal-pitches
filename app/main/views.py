from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User
from .forms import UpdateProfile,CommentForm
from ..import db,photos

# Views
@main.route('/')
def index():


  '''
  View root page function that returns the index page and its data
  '''

  pitches=[
      {
          'author':"Sunday Brian0",
          'title':'MatchdayExperience',
          'content':'Lorem Lorem',
          'date_posted':'July 13,2019'
      },
        {
          'author':"Sunday Brian1",
          'title':'MatchdayExperience',
          'content':'Lorem Lorem',
          'date_posted':'July 13,2019'
      },
        {
          'author':"Sunday Brian2",
          'title':'MatchdayExperience',
          'content':'Lorem Lorem',
          'date_posted':'July 13,2019'
      },
        {
          'author':"Sunday Brian3",
          'title':'MatchdayExperience',
          'content':'Lorem Lorem',
          'date_posted':'July 13,2019'
      }
  ]
  return render_template('index.html',title='home',pitches=pitches)

@main.route('/pitch/comment/new/<int:id>',methods=['GET','POST'])
@login_required
def new_comment(id):

  '''
  View function that returns a form to create a comment for a post
  '''
  form=CommentForm()
  


@main.route('/user/<uname>')
def profile(uname):

  '''
  View function for a user profile
  '''
  user=User.query.filter_by(username=uname).first()
  if user is None:
    abort(404)
  return render_template('profile/profile.html',user=user)  


@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
  '''
  update_profile view function 
  '''
  user=User.query.filter_by(username=uname).first()
  if user is None:
    abort(404)

  form=UpdateProfile()

  if form.validate_on_submit():
    user.bio=form.bio.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile',uname=user.username))

  return render_template('profile/update.html',form=form)    


@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def update_pic(uname):
  user=User.query.filter_by(username=uname).first()
  if 'photo' in request.files:
    filename=photos.save(request.files['photo'])
    path=f'photos/{filename}'
    user.profile_pic_path=path
    db.session.commit()
  return redirect(url_for('main.profile',uname=uname))  





