from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required, Length


class PitchForm(FlaskForm):
    pitch = TextAreaField('New Pitch', validators=[Required(), Length(max=150)])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')


class DeleteUser(FlaskForm):
    submit = SubmitField('Delete account')