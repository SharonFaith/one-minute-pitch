from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class DeleteUser(FlaskForm):
    submit = SubmitField('Delete account')