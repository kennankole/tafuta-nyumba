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

    def __repr__(self) -> str:
        return f"{self.units} unit(s) available @{self.price}each.\nOwner's contacts\n 1: {self.contacts} 2: {self.alternate_contact}"

    @staticmethod
    def constituency_results(const, rent, hse_type):
        if (
            Houses.query.filter_by(
                constituency=const, for_rent=rent, type_of_house=hse_type
            ).count()
            > 2
        ):
            return str(
                Houses.query.filter_by(
                    constituency=const, for_rent=rent, type_of_house=hse_type
                )
                .order_by(func.random())
                .limit(2)
                .all()
            )[1:-1]

        if (
            0
            < Houses.query.filter_by(
                constituency=const, for_rent=rent, type_of_house=hse_type
            ).count()
            <= 2
        ):
            return str(
                Houses.query.filter_by(
                    constituency=const, for_rent=rent, type_of_house=hse_type
                ).all()
            )[1:-1]

        if not Houses.query.filter_by(
            constituency=const, for_rent=rent, type_of_house=hse_type
        ):
            return "No records at the moment\nTry again later\n"

    @staticmethod
    def ward_results(ward, rent, hse_type):
        if (
            Houses.query.filter_by(
                ward=ward, for_rent=rent, type_of_house=hse_type
            ).count()
            > 2
        ):
            return str(
                Houses.query.filter_by(ward=ward, for_rent=rent, type_of_house=hse_type)
                .order_by(func.random())
                .limit(2)
                .all()
            )[1:-1]

        if (
            0
            < Houses.query.filter_by(
                ward=ward, for_rent=rent, type_of_house=hse_type
            ).count()
            <= 2
        ):
            return str(
                Houses.query.filter_by(
                    ward=ward, for_rent=rent, type_of_house=hse_type
                ).all()
            )[1:-1]

        if not Houses.query.filter_by(ward=ward, for_rent=rent, type_of_house=hse_type):
            return "No records at the moment\nTry again later\n"

    @staticmethod
    def village_estate_results(village_estate, rent, hse_type):
        if (
            Houses.query.filter_by(
                name_of_estate_or_village=village_estate,
                for_rent=rent,
                type_of_house=hse_type,
            ).count()
            > 2
        ):
            return str(
                Houses.query.filter_by(
                    ward=village_estate, for_rent=rent, type_of_house=hse_type
                )
                .order_by(func.random())
                .limit(2)
                .all()
            )[1:-1]

        if (
            0
            < Houses.query.filter_by(
                name_of_estate_or_village=village_estate,
                for_rent=rent,
                type_of_house=hse_type,
            ).count()
            <= 2
        ):
            return str(
                Houses.query.filter_by(
                    name_of_estate_or_village=village_estate,
                    for_rent=rent,
                    type_of_house=hse_type,
                ).all()
            )[1:-1]

        if not Houses.query.filter_by(
            name_of_estate_or_village=village_estate,
            for_rent=rent,
            type_of_house=hse_type,
        ):
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

    def __repr__(self) -> str:
        return f"{self.units} unit(s) available @{self.price}each.\nOwner's contacts\n 1: {self.contacts} 2: {self.alternate_contact}"

    @staticmethod
    def constituency_results(const):
        if Hostels.query.filter_by(constituency=const).count() > 2:
            return str(
                Hostels.query.filter_by(constituency=const)
                .order_by(func.random())
                .limit(2)
                .all()
            )[1:-1]

        if 0 < Hostels.query.filter_by(constituency=const).count() <= 2:
            return str(Hostels.query.filter_by(constituency=const).all())[1:-1]

        if not Hostels.query.filter_by(constituency=const):
            return "No records at the moment\nTry again later\n"

    @staticmethod
    def ward_results(ward):
        if Hostels.query.filter_by(ward=ward).count() > 2:
            return str(
                Hostels.query.filter_by(ward=ward)
                .order_by(func.random())
                .limit(2)
                .all()
            )[1:-1]

        if 0 < Hostels.query.filter_by(ward=ward).count() <= 2:
            return str(Hostels.query.filter_by(ward=ward).all())[1:-1]

        if not Hostels.query.filter_by(ward=ward):
            return "No records at the moment\nTry again later\n"

    @staticmethod
    def school_query_results(schl_name):
        if Hostels.query.filter_by(school_name=schl_name).count() > 2:
            return str(
                Hostels.query.filter_by(school_name=schl_name)
                .order_by(func.random())
                .limit(2)
                .all()
            )[1:-1]

        if 0 < Hostels.query.filter_by(school_name=schl_name).count() <= 2:
            return str(Hostels.query.filter_by(school_name=schl_name).all())[1:-1]

        if not Hostels.query.filter_by(school_name=schl_name):
            return "No records at the moment\nTry again later\n"


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

    @staticmethod
    def constituency_results(const, rent, biz_type):
        if (
            BusinessPremises.query.filter_by(
                constituency=const, for_rent=rent, type_of_business_premise=biz_type
            ).count()
            > 2
        ):
            return str(
                BusinessPremises.query.filter_by(
                    constituency=const, for_rent=rent, type_of_business_premise=biz_type
                )
                .order_by(func.random())
                .limit(2)
                .all()
            )[1:-1]

        if (
            0
            < BusinessPremises.query.filter_by(
                constituency=const, for_rent=rent, type_of_business_premise=biz_type
            ).count()
            <= 2
        ):
            return str(
                BusinessPremises.query.filter_by(
                    constituency=const, for_rent=rent, type_of_business_premise=biz_type
                ).all()
            )[1:-1]

        if not BusinessPremises.query.filter_by(
            constituency=const, for_rent=rent, type_of_business_premise=biz_type
        ):
            return "No records at the moment\nTry again later\n"

    @staticmethod
    def ward_results(ward, rent, biz_type):
        if (
            BusinessPremises.query.filter_by(
                ward=ward, for_rent=rent, type_of_business_premise=biz_type
            ).count()
            > 2
        ):
            return str(
                BusinessPremises.query.filter_by(
                    ward=ward, for_rent=rent, type_of_business_premise=biz_type
                )
                .order_by(func.random())
                .limit(2)
                .all()
            )[1:-1]

        if (
            0
            < BusinessPremises.query.filter_by(
                ward=ward, for_rent=rent, type_of_business_premise=biz_type
            ).count()
            <= 2
        ):
            return str(
                BusinessPremises.query.filter_by(
                    ward=ward, for_rent=rent, type_of_business_premise=biz_type
                ).all()
            )[1:-1]

        if not BusinessPremises.query.filter_by(
            ward=ward, for_rent=rent, type_of_business_premise=biz_type
        ):
            return "No records at the moment\nTry again later\n"

    @staticmethod
    def city_or_town_results(city_or_town, rent, biz_type):
        if (
            BusinessPremises.query.filter_by(
                name_of_city_or_town=city_or_town,
                for_rent=rent,
                type_of_business_premise=biz_type,
            ).count()
            > 2
        ):
            return str(
                BusinessPremises.query.filter_by(
                    name_of_city_or_town=city_or_town,
                    for_rent=rent,
                    type_of_business_premise=biz_type,
                )
                .order_by(func.random())
                .limit(2)
                .all()
            )[1:-1]

        if (
            0
            < BusinessPremises.query.filter_by(
                name_of_city_or_town=city_or_town,
                for_rent=rent,
                type_of_business_premise=biz_type,
            ).count()
            <= 2
        ):
            return str(
                BusinessPremises.query.filter_by(
                    name_of_city_or_town=city_or_town,
                    for_rent=rent,
                    type_of_business_premise=biz_type,
                ).all()
            )[1:-1]

        if not BusinessPremises.query.filter_by(
            name_of_city_or_town=city_or_town,
            for_rent=rent,
            type_of_business_premise=biz_type,
        ):
            return "No records at the moment\nTry again later\n"


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
