from app.business.biz_query_menu import BusinessPremisesQueryMenu
from app.business.data import types_of_business_premises
from sqlalchemy.sql import func
from app.business.utils import get_type_of_business_premises
from app.decorators.location import location_decorator
from app.decorators.names import names_decorator
from app.decorators.payment_decorators import charge_users_decorator
from app.models import BusinessPremises
from app.utils import storing_user_records


class BusinessPremisesQueryResults(BusinessPremisesQueryMenu):
    @charge_users_decorator
    @names_decorator(level=201, message="Enter name of city or town\n")
    # @location_decorator(level=201, message="Enter name of city or town\n")
    def biz_premises_city_or_town_results(self):
        rent = bool
        biz_id = self.session.get("biz_type")
        city_or_town = self.user_response
        if self.session.get("rent_business"):
            rent = True
            service_type = "renting"
        if self.session.get("buy_business"):
            rent = False
            service_type = "buying"
        storing_user_records(
            self.phone_number,
            service_type,
            get_type_of_business_premises(biz_id, types_of_business_premises),
        )
        if BusinessPremises.query.filter_by(name_of_city_or_town=city_or_town, for_rent=rent, type_of_business_premise=get_type_of_business_premises(biz_id, types_of_business_premises)) > 2:
            menu_text = f"{get_type_of_business_premises(biz_id, types_of_business_premises)} in {city_or_town}\n"
            menu_text += f"{str(BusinessPremises.query.filter_by(name_of_city_or_town=city_or_town, for_rent=rent, type_of_business_premise=get_type_of_business_premises(biz_id, types_of_business_premises)).order_by(func.random()).limit(2).all())[1:-1]}"
            menu_text += "Re-enter name of the city to see more results\n"
            menu_text += f"{city_or_town.title()} >> (next)\n"
            return self.ussd_continue(menu_text)
        
        if 0 < BusinessPremises.query.filter_by(name_of_city_or_town=city_or_town, for_rent=rent, type_of_business_premise=get_type_of_business_premises(biz_id, types_of_business_premises)).count() <= 2:
            menu_text = f"{str(BusinessPremises.query.filter_by(name_of_city_or_town=city_or_town, for_rent=rent, type_of_business_premise=get_type_of_business_premises(biz_id, types_of_business_premises)).all())[1:-1]}"
            return self.ussd_end(menu_text)
        
        else:
            menu_text = "No records\nKindly try again later\n"
            return self.ussd_end(menu_text)

    @charge_users_decorator
    @location_decorator(level=202, message="Enter Constituency")
    def biz_premises_const_query_results(self):
        rent = bool
        biz_id = self.session.get("biz_type")
        const = self.user_response
        if self.session.get("rent_business"):
            rent = True
            service_type = "renting"
        if self.session.get("buy_business"):
            rent = False
            service_type = "buying"
        storing_user_records(
            self.phone_number,
            service_type,
            get_type_of_business_premises(biz_id, types_of_business_premises),
        )
        if BusinessPremises.query.filter_by(constituency=const, for_rent=rent, type_of_business_premise=get_type_of_business_premises(biz_id, types_of_business_premises)) > 2:
            menu_text = f"{get_type_of_business_premises(biz_id, types_of_business_premises)} in {const}\n"
            menu_text += f"{str(BusinessPremises.query.filter_by(constituency=const, for_rent=rent, type_of_business_premise=get_type_of_business_premises(biz_id, types_of_business_premises)).order_by(func.random()).limit(2).all())[1:-1]}"
            menu_text += "Re-enter constituency name to see more results\n"
            menu_text += f"{const.title()} >> (next)\n"
            return self.ussd_continue(menu_text)
        
        if 0 < BusinessPremises.query.filter_by(constituency=const, for_rent=rent, type_of_business_premise=get_type_of_business_premises(biz_id, types_of_business_premises)).count() <= 2:
            menu_text = f"{str(BusinessPremises.query.filter_by(constituency=const, for_rent=rent, type_of_business_premise=get_type_of_business_premises(biz_id, types_of_business_premises)).all())[1:-1]}"
            return self.ussd_end(menu_text)
        
        else:
            menu_text = "No records\nKindly try again later\n"
            return self.ussd_end(menu_text)


    @charge_users_decorator
    @location_decorator(level=203, message="Enter Ward")
    def biz_premises_ward_query_results(self):
        rent = bool
        biz_id = self.session.get("biz_type")
        ward = self.user_response
        if self.session.get("rent_business"):
            rent = True
            service_type = "renting"
        if self.session.get("buy_business"):
            rent = False
            service_type = "buying"
        storing_user_records(
            self.phone_number,
            service_type,
            get_type_of_business_premises(biz_id, types_of_business_premises),
        )
    
        if BusinessPremises.query.filter_by(ward=ward, for_rent=rent, type_of_business_premise=get_type_of_business_premises(biz_id, types_of_business_premises)) > 2:
            menu_text = f"{get_type_of_business_premises(biz_id, types_of_business_premises)} in {ward}\n"
            menu_text += f"{str(BusinessPremises.query.filter_by(ward=ward, for_rent=rent, type_of_business_premise=get_type_of_business_premises(biz_id, types_of_business_premises)).order_by(func.random()).limit(2).all())[1:-1]}"
            menu_text += "Re-enter ward name to see more results\n"
            menu_text += f"{ward.title()} >> (next)\n"
            return self.ussd_continue(menu_text)
        
        if 0 < BusinessPremises.query.filter_by(ward=ward, for_rent=rent, type_of_business_premise=get_type_of_business_premises(biz_id, types_of_business_premises)).count() <= 2:
            menu_text = f"{str(BusinessPremises.query.filter_by(ward=ward, for_rent=rent, type_of_business_premise=get_type_of_business_premises(biz_id, types_of_business_premises)).all())[1:-1]}"
            return self.ussd_end(menu_text)
        
        else:
            menu_text = "No records\nKindly try again later\n"
            return self.ussd_end(menu_text)
    
    def execute(self):
        level = self.session.get("level")
        menu = {
            201: self.biz_premises_city_or_town_results,
            202: self.biz_premises_const_query_results,
            203: self.biz_premises_ward_query_results,
        }
        return menu.get(level, self.search_business_premises_by_location)()
