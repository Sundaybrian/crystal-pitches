from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required
from wtforms import ValidationError



class UpdateProfile(FlaskForm):
    bio=TextAreaField('Tell us about you',validators=[Required()])
    submit=SubmitField('Submit')



