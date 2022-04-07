import enum
from datetime import datetime
from sqlalchemy.sql import func
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import geojson
from app import db

hostel_assets = db.Table('hostel_assets',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='cascade'), primary_key=True),
    db.Column('hostels_id', db.Integer, db.ForeignKey('hostels.id', ondelete='cascade'), primary_key=True),
)

house_assets = db.Table('house_assets',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('houses_id', db.Integer, db.ForeignKey('houses.id'), primary_key=True),
)

business_assets = db.Table('business_assets',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('houses_id', db.Integer, db.ForeignKey('business_premises.id'), primary_key=True),
)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unique_id = db.Column(db.String())
    name = db.Column(db.String(), index=True)
    email = db.Column(db.String(), index=True)
    profile_pic = db.Column(db.String())
    created_on = db.Column(db.DateTime, unique=False)
    hostel_asset = db.relationship('Hostels', secondary=hostel_assets, backref=db.backref('hostel_assets', lazy=True))
    house_asset = db.relationship('Houses', secondary=house_assets, backref=db.backref('houses_assets', lazy=True))
    business_premises_asset = db.relationship('BusinessPremises', secondary=business_assets, backref=db.backref('premises_assets', lazy=True))
    
    
    @staticmethod
    def create(id, name, email, profile_pic):
        user = User(id, name, email, profile_pic)
        db.session.add(user)
        db.session.commit()
    
    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    

    def get_id(self):
        '''
        Should match the load_user
        '''
        return self.unique_id
    
    def __repr__(self) -> str:
        return f'<User {self.name}>'
    


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
    image = db.Column(db.String(), nullable=True)

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
    

class ListingStatus(enum.Enum):
    rent_out = 'Rent out'
    sale = 'Sale'
class Hostels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    county = db.Column(db.String(64), index=True)
    constituency = db.Column(db.String(150), index=True)
    ward = db.Column(db.String(150), index=True)
    school_name = db.Column(db.String(150), index=True)
    units = db.Column(db.Integer, index=True)
    price = db.Column(db.Integer, index=True)
    listing_status = db.Column(db.Enum(ListingStatus), default=ListingStatus.rent_out)
    contacts = db.Column(db.String(64), index=True)
    alternate_contact = db.Column(db.String(64), index=True)
    photo = db.Column(db.String(), default='two_bedroom.jpg')
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    gallery = db.relationship('HostelsGallery',  backref='hostels', lazy=True)

    def __repr__(self) -> str:
        return f"{self.units} unit(s) available @{self.price} each.\nOwner's contacts\n 1: {self.contacts} 2: {self.alternate_contact}"

    
    @staticmethod
    def get_const_hostels(const):
        if Hostels.query.filter_by(constituency=const).count() > 2:
            return str(Hostels.query.filter_by(constituency=const).order_by(func.random()).limit(2).all())[1:-1]
        
        elif 0 < Hostels.query.filter_by(constituency=const).count() <= 2:
            return str(Hostels.query.filter_by(constituency=const).all())[1:-1]
        
        else:
            return "No records\nKindly try again later\n"
        
    @staticmethod
    def get_hostels_school_name(name):
        if Hostels.query.filter_by(school_name=name).count() > 2:
            return str(Hostels.query.filter_by(school_name=name).order_by(func.random()).limit(2).all())[1:-1]
        
        elif 0 < Hostels.query.filter_by(school_name=name).count() <= 2:
            return str(Hostels.query.filter_by(school_name=name).all())[1:-1]
        
        else:
            return "No records\nKindly try again later\n"
       
       
    @staticmethod
    def get_ward_hostels(ward):
        if Hostels.query.filter_by(ward=ward).count() > 2:
            return str(Hostels.query.filter_by(ward=ward).order_by(func.random()).limit(2).all())[1:-1]
        
        elif 0 < Hostels.query.filter_by(ward=ward).count() <= 2:
            return str(Hostels.query.filter_by(ward=ward).all())[1:-1]
        
        else:
            return "No records\nKindly try again later\n"
      
    def charge_users(self, units, price):
        return 0.05 * (units * price)
    
    def test_charge_uses(self, units=1, price=1):
        return units * price
    
    
    def get_all__hostel_coordinates_to_geojson(self):
        list_ = []
        try:
            for i in Hostels.query.all():
                list_.append((i.latitude, i.longitude))
            my_point = geojson.MultiPoint(list_)
            return geojson.Feature(geometry=my_point)
        except:
            return None
    
    def get_hostel_coordinate_to_geojson(self, id):
        coord = Hostels.query.filter_by(id=id).first_or_404()
        coord_ = geojson.Point((coord.longitude, coord.latitude))
        return geojson.Feature(geometry=coord_)
    
class HostelsGallery(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String())
    description = db.Column(db.String(100))
    house_id = db.Column(db.Integer, db.ForeignKey('hostels.id'))
    
    def __repr__(self) -> str:
        return self.description
    
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
    photo = db.Column(db.String(), nullable=True)
    
    def __repr__(self) -> str:
        return f"{self.units} unit(s) available @{self.price} each.\nOwner's contacts\n1: {self.contacts} 2: {self.alternate_contact}"


    @staticmethod
    def get_const_business(const, rent, hse_type):
        if BusinessPremises.query.filter_by(constituency=const, for_rent=rent,  type_of_business_premise=hse_type).count() > 2:
            return str(BusinessPremises.query.filter_by(constituency=const, for_rent=rent,  type_of_business_premise=hse_type).order_by(func.random()).limit(2).all())[1:-1]
        
        elif 0 < BusinessPremises.query.filter_by(constituency=const, for_rent=rent,  type_of_business_premise=hse_type).count() <= 2:
            return str(BusinessPremises.query.filter_by(constituency=const, for_rent=rent,  type_of_business_premise=hse_type).all())[1:-1]
        
        else:
            return "No records\nKindly try again later\n"
        
        
    @staticmethod
    def get_ward_business(ward, rent, hse_type):
        if BusinessPremises.query.filter_by(ward=ward, for_rent=rent,  type_of_business_premise=hse_type).count() > 2:
            return str(BusinessPremises.query.filter_by(ward=ward, for_rent=rent,  type_of_business_premise=hse_type).order_by(func.random()).limit(2).all())[1:-1]
        
        elif 0 < BusinessPremises.query.filter_by(ward=ward, for_rent=rent,  type_of_business_premise=hse_type).count() <= 2:
            return str(BusinessPremises.query.filter_by(ward=ward, for_rent=rent,  type_of_business_premise=hse_type).all())[1:-1]
        
        else:
            return "No records\nKindly try again later\n"
       
       
    @staticmethod
    def get_name_of_city_business(name, rent, hse_type):
        if BusinessPremises.query.filter_by(name_of_city_or_town=name, for_rent=rent,  type_of_business_premise=hse_type).count() > 2:
            return str(BusinessPremises.query.filter_by(name_of_city_or_town=name, for_rent=rent,  type_of_business_premise=hse_type).order_by(func.random()).limit(2).all())[1:-1]
        
        elif 0 < BusinessPremises.query.filter_by(name_of_city_or_town=name, for_rent=rent,  type_of_business_premise=hse_type).count() <= 2:
            return str(BusinessPremises.query.filter_by(name_of_city_or_town=name, for_rent=rent,  type_of_business_premise=hse_type).all())[1:-1]
        
        else:
            return "No records\nKindly try again later\n"
        
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


class PaymentDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    description = db.Column(db.String(64))
    type = db.Column(db.String(64))
    reference = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    middle_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    phone_number = db.Column(db.String(64))
    organization_balance = db.Column(db.Integer)
    

class JsonFeature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    
    def __repr__(self):
        return f"{(self.latitude, self.longitude)}"

    
    def get_all_coordinates_to_geojson(self):
        list_ = []
        for i in JsonFeature.query.all():
            list_.append((i.latitude, i.longitude))
        my_point = geojson.MultiPoint(list_)
        return geojson.Feature(geometry=my_point)
    
    def get_property_location(self, id):
        coord = JsonFeature.query.filter_by(id=id).first_or_404()
        coord_ = geojson.Point((coord.longitude, coord.latitude))
        return geojson.Feature(geometry=coord_)


class PaymentPlanStatus(enum.Enum):
    weekly = 'Weekly'
    monthly = 'Monthly'
    annually = 'Annually' 
    
    
class ServiceTypeStatus(enum.Enum):
    rent_out = 'Rent Out'
    sell = 'Sell'
class PaymentPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    type_of_property = db.Column(db.String())
    units = db.Column(db.Integer)
    price = db.Column(db.Integer)
    plan = db.Column(db.Enum(PaymentPlanStatus))
    amount = db.Column(db.Float)
    service_type = db.Column(db.Enum(ServiceTypeStatus))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    def __repr__(self) -> str:
        return f"{self.plan, self.price, self.latitude, self.longitude}"
    
    
    
    