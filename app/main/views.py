from flask import render_template,request,redirect,url_for,abort,flash,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Posts,Comment
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


@main.route('/pitch/<int:pitch_id>')
def post(pitch_id):
  post=Posts.query.get(pitch_id)

  return render_template('pitch.html',title=post.post_title, pitch=post)


@main.route('/pitch/comment/new/<int:pitch_id>',methods=['GET','POST'])
@login_required
def new_comment(pitch_id):

  '''
  View function that returns a form to create a comment for a post
  '''
  post=Posts.query.filter_by(post_id=pitch_id)
  form=CommentForm()

  if form.validate_on_submit():
    comment_content=form.comment_content.data
    new_comment=Comment(comment_content=comment_content,pitch=post,user=current_user)

    return redirect(url_for('.post',pitch_id=post.id))


  return render_template('new_comment.html',title='New Comment',comment_form=form)  



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





