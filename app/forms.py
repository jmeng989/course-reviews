from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    SelectField,
    IntegerField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Regexp, NumberRange, Optional, ValidationError

class LoginForm(FlaskForm):
    username = StringField('CRSID', validators=[DataRequired(), Regexp(r'^[A-Za-z]+[0-9]+$')])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class ReviewForm(FlaskForm):
    part = SelectField('Part', choices=[('', 'All parts')], validators=[Optional()])
    course_id = SelectField('Course', coerce=int, validators=[DataRequired()])
    year = IntegerField('Academic year', validators=[DataRequired(), NumberRange(min=2000, max=2100)])
    fun = SelectField(
        'Fun',
        choices=[(str(value), f'{value / 2:g} stars') for value in range(2, 11)],
        coerce=int,
        validators=[DataRequired(), NumberRange(min=2, max=10)],
    )
    difficulty = SelectField(
        'Difficulty',
        choices=[(str(value), f'{value / 2:g} stars') for value in range(2, 11)],
        coerce=int,
        validators=[DataRequired(), NumberRange(min=2, max=10)],
    )
    content = TextAreaField('Review', validators=[DataRequired()])
    lecturer_content = TextAreaField(
        'Lecturer review (optional)', validators=[Optional()]
    )
    submit = SubmitField('Submit review')

    def validate_course_id(self, field):
        if field.data not in {course_id for course_id, _ in self.course_id.choices}:
            raise ValidationError('Select a valid course.')