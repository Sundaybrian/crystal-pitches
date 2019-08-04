from flask import render_template,request,redirect,url_for,abort,flash,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Posts
from .forms import UpdateProfile,CommentForm,PostForm
from ..import db,photos

# Views
@main.route('/')
def index():

  '''
  View root page function that returns the index page and its data
  '''
  pitches=Posts.query.all()
  return render_template('index.html',title='home',pitches=pitches)


@main.route('/pitch/new',methods=['GET','POST']) 
@login_required
def new_post():
  form=PostForm()

  if form.validate_on_submit():
    post_title=form.post_title.data
    post_content=form.post_content.data
    new_post=Posts(post_title=post_title,post_content=post_content,user=current_user)
    new_post.save_post()

    flash('Your pitch was created successfully')
    return redirect(url_for('.index'))

  return render_template('create_post.html',title='New Pitch',create_form=form)  



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





