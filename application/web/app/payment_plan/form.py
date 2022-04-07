from flask_wtf import FlaskForm
from wtforms.fields import SelectField, FloatField, IntegerField, StringField, SubmitField

 
PPLAN_CHOICES = [
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('annually', 'Annually')
]

TYP_SERVICE_CHOICES = [
    ('rent', 'Rent Out'),
    ('sell', 'Sell'),
]

class PaymentPlanForm(FlaskForm):
    plan = SelectField('Plan',choices=PPLAN_CHOICES)
    service_type = SelectField('Service',choices=TYP_SERVICE_CHOICES)
    latitude = FloatField('latitude')
    longitude = FloatField('longitude')
    type_of_property = StringField('Property Type', default='Hostel')
    units = IntegerField('Units')
    price = IntegerField('Price')
    amount = FloatField('Amount')
    submit = SubmitField('Submit')