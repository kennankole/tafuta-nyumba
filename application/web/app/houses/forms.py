import json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.fields.simple import BooleanField, TelField
from wtforms.validators import DataRequired, Length, ValidationError

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
    

class HouseRegistrationForm(FlaskForm):
    RENTING = [
        (1, "Yes"),
        (2, "No")
    ]
    county = StringField('County', [DataRequired(), validate_names, validate_location])
    constituency = StringField('Constituency', [DataRequired(), validate_names, validate_location])
    ward = StringField('Ward', [DataRequired(), validate_names, validate_location])
    name_of_estate_or_village = StringField('Name of estate or village', [DataRequired(), validate_names])
    type_of_house = StringField('Type of house', [DataRequired(), validate_names])
    units = IntegerField('Units', [DataRequired(), validate_int_fields])
    price = IntegerField('Price', [DataRequired(), validate_int_fields])
    alternate_contact = TelField('Mobile number', [DataRequired()])
    for_rent = BooleanField('Are you selling this property?', [DataRequired()] )
    submit = SubmitField('Register')
        
    
class UpdateHousesForm(FlaskForm):
    units = IntegerField('Units', [DataRequired(), validate_int_fields])
    price = IntegerField('Price', [DataRequired(), validate_int_fields])
    alternate_contact = TelField('Mobile number', [DataRequired()])
    for_rent = BooleanField('Are you selling this property?', [DataRequired()] )
    submit = SubmitField('Update')
    

    
    