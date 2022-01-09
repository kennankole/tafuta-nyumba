from datetime import datetime

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

    def __repr__(self):
        return f"{self.units} unit(s) available @{self.price} each.\nOwner's contacts\n{self.contacts}/{self.alternate_contact}\n"

    @staticmethod
    def get_const_houses(const, rent, hse_type):
        if Houses.query.filter_by(constituency=const, for_rent=rent, type_of_house=hse_type).count() > 2:
            return str(Houses.query.filter_by(constituency=const, for_rent=rent, type_of_house=hse_type).order_by(func.random()).limit(2).all())[1:-1]
        
        elif 0 < Houses.query.filter_by(constituency=const, for_rent=rent, type_of_house=hse_type).count() <= 2:
            return str(Houses.query.filter_by(constituency=const, for_rent=rent, type_of_house=hse_type).all())[1:-1]
        
        else:
            return "No records\nKindly try again later\n"
        
    @staticmethod
    def get_village_houses(name, rent, hse_type):
        if Houses.query.filter_by(name_of_estate_or_village=name, for_rent=rent, type_of_house=hse_type).count() > 2:
            return str(Houses.query.filter_by(name_of_estate_or_village=name, for_rent=rent, type_of_house=hse_type).order_by(func.random()).limit(2).all())[1:-1]
        
        elif 0 < Houses.query.filter_by(name_of_estate_or_village=name, for_rent=rent, type_of_house=hse_type).count() <= 2:
            return str(Houses.query.filter_by(name_of_estate_or_village=name, for_rent=rent, type_of_house=hse_type).all())[1:-1]
        
        else:
            return "No records\nKindly try again later\n"
       
       
    @staticmethod
    def get_ward_houses(ward, rent, hse_type):
        if Houses.query.filter_by(ward=ward, for_rent=rent, type_of_house=hse_type).count() > 2:
            return str(Houses.query.filter_by(ward=ward, for_rent=rent, type_of_house=hse_type).order_by(func.random()).limit(2).all())[1:-1]
        
        elif 0 < Houses.query.filter_by(ward=ward, for_rent=rent, type_of_house=hse_type).count() <= 2:
            return str(Houses.query.filter_by(ward=ward, for_rent=rent, type_of_house=hse_type).all())[1:-1]
        
        else:
            return "No records\nKindly try again later\n"
    
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

    def __repr__(self) -> str:
        return f"{self.units} unit(s) available @{self.price} each.\nOwner's contacts\n 1: {self.contacts} 2: {self.alternate_contact}"

    
    
class BusinessPremises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    county = db.Column(db.String(64), index=True)
    constituency = db.Column(db.String(150), index=True)
    ward = db.Column(db.String(150), index=True)
    name_of_city_or_town = db.Column(db.String(150), index=True)
    street_name = db.Column(db.String(254), index=True)
    type_of_business_premise = db.Column(db.String(250), index=True)
    area = db.Column(db.Integer, index=True)
    units = db.Column(db.Integer, index=True)
    price = db.Column(db.Integer, index=True)
    contacts = db.Column(db.String(64), index=True)
    alternate_contact = db.Column(db.String(64), index=True)
    for_rent = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return f"{self.units} unit(s) available @{self.price} each.\nOwner's contacts\n1: {self.contacts} 2: {self.alternate_contact}"


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


class CapturingUserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contacts = db.Column(db.String(64), index=True)
    service_type = db.Column(db.String(64), index=True)
    property_type = db.Column(db.String(64), index=True)
    accessed_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return (
            f"{self.contacts, self.service_type, self.property_type, self.accessed_at}"
        )
