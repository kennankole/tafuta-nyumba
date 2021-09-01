from app import db 
from sqlalchemy.sql import func

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

    @staticmethod
    def constituency_results(const, rent, hse_type):
        if Houses.query.filter_by(
            constituency=const, for_rent=rent, type_of_house=hse_type
        ).count() > 2:
            return str(Houses.query.filter_by(constituency=const, for_rent=rent, type_of_house=hse_type).order_by(func.random()).limit(2).all())[1:-1]
            
        if 0 < Houses.query.filter_by(
            constituency=const, for_rent=rent, type_of_house=hse_type
        ).count() <= 2:
            return str(Houses.query.filter_by(constituency=const, for_rent=rent, type_of_house=hse_type).all())[1:-1]
        
        if not Houses.query.filter_by(constituency=const, for_rent=rent, type_of_house=hse_type):
            return "No records at the moment\nTry again later\n"
        


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