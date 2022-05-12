from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Add some bio about you.',validators = [DataRequired()])
    submit = SubmitField('Save')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Business','Business'),('Meet_Greet','Meet_Greet'),('Interviews','Interviews')],validators=[DataRequired()])
    post = TextAreaField(' Add Your Pitch', validators=[DataRequired()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[DataRequired()])
    submit = SubmitField('Comment')