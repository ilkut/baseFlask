from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from app.models import User, Note


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')

class NoteForm(FlaskForm):
    note = TextAreaField(('Say something'), validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(('Submit'))
