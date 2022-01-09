from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.fields.simple import TelField
from wtforms.validators import DataRequired

from app.houses import forms as form

class HostelRegistrationForm(FlaskForm):
    county = StringField('County', [DataRequired(), form.validate_names, form.validate_location])
    constituency = StringField('Constituency', [DataRequired(), form.validate_names, form.validate_location])
    ward = StringField('Ward', [DataRequired(), form.validate_names, form.validate_location])
    school_name = StringField('Name School', [DataRequired(), form.validate_names])
    units = IntegerField('Units', [DataRequired(), form.validate_int_fields])
    price = IntegerField('Price', [DataRequired(), form.validate_int_fields])
    alternate_contact = TelField('Mobile number', [DataRequired()])
    submit = SubmitField('Register')
    
    
class HostelUpdateForm(FlaskForm):
    units = IntegerField('Units', [DataRequired(), form.validate_int_fields])
    price = IntegerField('Price', [DataRequired(), form.validate_int_fields])
    alternate_contact = TelField('Mobile number', [DataRequired()])
    submit = SubmitField('Register')
    