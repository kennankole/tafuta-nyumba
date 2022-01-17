import json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.fields.simple import TelField
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms.validators import DataRequired

from app.houses import forms as form

from app.location import location


def validate_int_fields(form, field):
    if field.data is not None:
        if field.data < 0:
            raise ValidationError("Invalid Input!! Values cannot be negative")
    
def validate_names(form, field):
    regex = "[0-9]~!@#$%^&*()_-+={[}]|\?/><.,"
    if any(i in regex for i in field.data):
        raise ValidationError("Invalid Input, names may not contain special characters")
    
    
def validate_location(form, field):
    counties = json.loads(location)
    if field.data not in counties.__str__():
        raise ValidationError(f"{field.data} is an invalid location")
    
class HostelRegistrationForm(FlaskForm):
    county = StringField('County', [DataRequired(), validate_location])
    constituency = StringField('Constituency', [DataRequired(), validate_location])
    ward = StringField('Ward', [DataRequired(), form.validate_names, validate_location])
    school_name = StringField('Name School', [DataRequired(), validate_names])
    units = IntegerField('Units', [DataRequired(), validate_int_fields])
    price = IntegerField('Price', [DataRequired(), validate_int_fields])
    alternate_contact = TelField('Mobile number', [DataRequired()])
    submit = SubmitField('Register')
    
    
class HostelUpdateForm(FlaskForm):
    units = IntegerField('Units', [DataRequired(), validate_int_fields])
    price = IntegerField('Price', [DataRequired(), validate_int_fields])
    alternate_contact = TelField('Mobile number', [DataRequired()])
    submit = SubmitField('Register')
    