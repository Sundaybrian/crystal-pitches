from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required




class PostForm(FlaskForm):
    '''
    Class to create a form for creating a pitch post
    '''
    post_title=StringField('Pitch Title',validators=[Required()])
    post_content=TextAreaField('Pitch Content',validators=[Required()])
    submit=SubmitField('Submit Pitch')


class CommentForm(FlaskForm):
    '''
    Class to create a comment form 
    '''
    comment_content=TextAreaField('Comment',validators=[Required()])
    submit=SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio=TextAreaField('Tell us about you',validators=[Required()])
    submit=SubmitField('Submit')



