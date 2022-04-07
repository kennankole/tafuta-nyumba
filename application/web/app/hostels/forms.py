from ast import For
import json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FieldList, Form, SelectField, FormField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename
from wtforms.validators import DataRequired
from app.models import Hostels


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


class ListingStatus(Form):
    listing_status = SelectField(choices=[
        ('rent out', 'Rent Out'),
        ('sale', 'Sale')
    ])
 
class HostelUpdateForm(FlaskForm):
    units = IntegerField('Units', [DataRequired(), validate_int_fields])
    price = IntegerField('Price', [DataRequired(), validate_int_fields])
    contacts = StringField('Mobile number 1', [DataRequired()])
    listing_status = FieldList(FormField(ListingStatus))
    alternate_contact = StringField('Mobile number 2', [DataRequired()])
    photo  = FileField('Picture')
    submit = SubmitField('Update')
    
    
    