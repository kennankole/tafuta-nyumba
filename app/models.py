from operator import index
from app import db 

class Houses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    county = db.Column(db.String(254), index=True)
    constituency = db.Column(db.String(254), index=True)
    ward = db.Column(db.String(150), index=True)
    name_of_estate_or_village = db.Column(db.String(254), index=True)
    type_of_house = db.Column(db.String(254), index=True)
    units = db.Column(db.Integer, index=True)
    price = db.Column(db.Integer, index=True)
    contacts = db.Column(db.String(64), index=True)
    alternate_contact = db.Column(db.String(64), index=True)
    for_rent = db.Column(db.Boolean, default=False)


class Hostels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    county = db.Column(db.String(64), index=True)
    constituency = db.Column(db.String(150), index=True)
    ward = db.Column(db.String(150), index=True)
    school_name = db.Column(db.String(150), index=True)
    units = db.Column(db.Integer, index=True)
    price = db.Column(db.Integer, index=True)
    contacts = db.Column(db.String(64), index=True)
    alternate_contact = db.Column(db.String(64), index=True)


class BusinessPremises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    county = db.Column(db.String(64), index=True)
    constituency = db.Column(db.String(150), index=True)
    ward = db.Column(db.String(150), index=True)
    street_name = db.Column(db.String(254), index=True)
    type_of_business_premise = db.Column(db.Integer, index=True)
    area = db.Column(db.Integer, index=True)
    units = db.Column(db.Integer, index=True)
    price = db.Column(db.Integer, index=True)
    contacts = db.Column(db.String(64), index=True)
    alternate_contact = db.Column(db.String(64), index=True)
    for_rent = db.Column(db.Boolean, default=False)
    
    
class Land(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    county = db.Column(db.String(64), index=True)
    constituency = db.Column(db.String(150), index=True)
    ward = db.Column(db.String(150), index=True)
    area = db.Column(db.Integer, index=True)
    plots = db.Column(db.Integer, index=True)
    price = db.Column(db.Integer, index=True)
    contacts = db.Column(db.String(64), index=True)
    alternate_contact = db.Column(db.String(64), index=True)
    for_rent = db.Column(db.Boolean, default=True)