from app.decorators.location import location_decorator
from app.decorators.names import names_decorator
from app.decorators.payment_decorators import charge_users_decorator
from app.houses.data import houses
from app.houses.houses_query_menu import HousesQueryMenu
from app.houses.utils import get_type_of_house
from app.models import Houses
from sqlalchemy.sql import func

from app.utils import storing_user_records


class HousesQueryResults(HousesQueryMenu):
    # @charge_users_decorator
    @location_decorator(level=21, message="Enter Constituency")
    def houses_const_query_results(self):
        rent = bool
        hse_id = self.session.get("hse_type")
        const = self.user_response
        if self.session.get("rent_house"):
            rent = True
            service_type = "renting"
        if self.session.get("buy_house"):
            rent = False
            service_type = "buying"
            
        storing_user_records(self.phone_number, service_type, get_type_of_house(hse_id, houses))
        house = Houses.query.filter_by(constituency=const, for_rent=rent, type_of_house=get_type_of_house(hse_id, houses)).count()
        if house > 2:
            menu_text = f"{Houses.get_const_houses(const=const, rent=rent, hse_type=get_type_of_house(hse_id, houses))}"
            menu_text += f"{get_type_of_house(hse_id, houses)} in {const}\n"
            menu_text += "Re-enter constituency name to see more results\n"
            menu_text += f"{const.title()} >> (next)\n"
            return self.ussd_continue(menu_text) 
        else:
            menu_text = f"{get_type_of_house(hse_id, houses)} in {const}\n"
            menu_text = f"{Houses.get_const_houses(const=const, rent=rent, hse_type=get_type_of_house(hse_id, houses))}"
            return self.ussd_end(menu_text)

        
    # @charge_users_decorator
    @location_decorator(level=22, message="Enter Ward")
    def houses_ward_query_results(self):
        rent = bool
        hse_id = self.session.get("hse_type")
        ward = self.user_response
        if self.session.get("rent_house"):
            rent = True
            service_type = "renting"
        if self.session.get("buy_house"):
            rent = False
            service_type = "buying"
        storing_user_records(self.phone_number, service_type,get_type_of_house(hse_id, houses))
        
        if Houses.query.filter_by(ward=ward, for_rent=rent, type_of_house=get_type_of_house(hse_id, houses)).count() > 2:
            menu_text = f"{Houses.get_const_houses(ward=ward, rent=rent, hse_type=get_type_of_house(hse_id, houses))}"
            menu_text += f"{get_type_of_house(hse_id, houses)} in {ward}\n"
            menu_text += "Re-enter constituency name to see more results\n"
            menu_text += f"{ward.title()} >> (next)\n"
            return self.ussd_continue(menu_text) 
        else:
            menu_text = f"{get_type_of_house(hse_id, houses)} in {ward}\n"
            menu_text = f"{Houses.get_ward_houses(ward=ward, rent=rent, hse_type=get_type_of_house(hse_id, houses))}"
            return self.ussd_end(menu_text)
    
        

    # @charge_users_decorator
    @names_decorator(level=23, message="Enter Estate or village name")
    def houses_village_estate_query_results(self):
        rent = bool
        hse_id = self.session.get("hse_type")
        estate = self.user_response
        if self.session.get("rent_house"):
            rent = True
            service_type = "renting"
        if self.session.get("buy_house"):
            rent = False
            service_type = "buying"
        storing_user_records(self.phone_number, service_type,get_type_of_house(hse_id, houses))
        
        if Houses.query.filter_by(name_of_estate_or_village=estate, for_rent=rent, type_of_house=get_type_of_house(hse_id, houses)).count() > 2:
            menu_text = f"{get_type_of_house(hse_id, houses)} in {estate}\n"
            menu_text += f"{Houses.get_village_houses(name=estate, rent=rent, hse_type=get_type_of_house(hse_id, houses))}"
            menu_text += "Re-enter estate  to see more results\n"
            menu_text += f"{estate.title()} >> (next)\n"
            return self.ussd_continue(menu_text)
        else:
            menu_text = f"{get_type_of_house(hse_id, houses)} in {estate}\n"
            menu_text = f"{Houses.get_village_houses(name=estate, rent=rent, hse_type=get_type_of_house(hse_id, houses))}"
            return self.ussd_end(menu_text)

    def execute(self):
        level = self.session.get("level")
        menu = {
            21: self.houses_const_query_results,
            22: self.houses_ward_query_results,
            23: self.houses_village_estate_query_results,
        }
        return menu.get(level, self.search_houses_by_location)()
