import json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.fields.simple import BooleanField, TelField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed

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
    

class BusinessPremisesRegistrationForm(FlaskForm):
    county = StringField('County', [DataRequired(), validate_names, validate_location])
    constituency = StringField('Constituency', [DataRequired(), validate_names, validate_location])
    ward = StringField('Ward', [DataRequired(), validate_names, validate_location])
    name_of_city_or_town = StringField('Name of estate or village', [DataRequired(), validate_names])
    street_name = StringField('Street name', [DataRequired(), validate_names])
    type_of_business_premise = StringField('Type of business premise', [DataRequired(), validate_names])
    area = IntegerField('Floor area', [DataRequired(), validate_int_fields])
    units = IntegerField('Units', [DataRequired(), validate_int_fields])
    price = IntegerField('Price', [DataRequired(), validate_int_fields])
    alternate_contact = TelField('Mobile number', [DataRequired()])
    for_rent = BooleanField('Are you selling this property?', [DataRequired()] )
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Register')
        
    
class BusinessPremisesUpdateForm(FlaskForm):
    units = IntegerField('Units', [DataRequired(), validate_int_fields])
    price = IntegerField('Price', [DataRequired(), validate_int_fields])
    alternate_contact = TelField('Mobile number', [DataRequired()])
    for_rent = BooleanField('Are you selling this property?', [DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Update')
    

    
  
    
    