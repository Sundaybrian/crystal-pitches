from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required
from wtforms import ValidationError


class CommentForm(FlaskForm):
    '''
    Class to create a comment form 
    '''
    comment_content=TextAreaField('Comment',validators=[Required()])
    submit=SubmitField('Submit')



class UpdateProfile(FlaskForm):
    bio=TextAreaField('Tell us about you',validators=[Required()])
    submit=SubmitField('Submit')



