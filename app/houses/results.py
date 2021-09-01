from app.houses.houses_query_menu import HousesQueryMenu
from app.models import Houses
from app.houses.data import type_of_houses
from app.houses.utils import get_type_of_house

class HousesQueryResults(HousesQueryMenu):

    def houses_const_query_results(self):
        rent = True
        hse_id = self.session.get('hse_type')
        const = self.user_response
        if self.session.get("rent_house"):
            rent = True
            service_type = "renting"
        if self.session.get("buy_house"):
            rent = False
            service_type = "buying"
        # storing_user_records(self.phone_number, service_type,get_type_of_house(type_of_houses, hse_id)) 
        menu_text = f"{get_type_of_house(hse_id, type_of_houses)} in {const}\n"
        menu_text += f"{Houses.constituency_results(const=const, rent=rent, hse_type=get_type_of_house(hse_id, type_of_houses))}\n"
        return self.ussd_continue(menu_text)


    def houses_ward_query_results(self):
        # rent = True
        hse_id = self.session.get('hse_type')
        ward = self.user_response
        if self.session.get("rent_house"):
            rent = True
            service_type = "renting"
        if self.session.get("buy_house"):
            rent = False
            service_type = "buying"
        # storing_user_records(self.phone_number, service_type,get_type_of_house(type_of_houses, hse_id)) 
        menu_text = f"{get_type_of_house(hse_id, type_of_houses)} in {ward}\n"
        menu_text += f"{Houses.constituency_results(const=ward, rent=rent, hse_type=get_type_of_house(hse_id, type_of_houses))}\n"
        return self.ussd_continue(menu_text)

    def houses_village_estate_query_results(self):
        # rent = True
        hse_id = self.session.get('hse_type')
        village_estate = self.user_response
        if self.session.get("rent_house"):
            rent = True
            service_type = "renting"
        if self.session.get("buy_house"):
            rent = False
            service_type = "buying"
        # storing_user_records(self.phone_number, service_type,get_type_of_house(type_of_houses, hse_id)) 
        menu_text = f"{get_type_of_house(hse_id, type_of_houses)} in {village_estate}\n"
        menu_text += f"{Houses.constituency_results(const=village_estate, rent=rent, hse_type=get_type_of_house(hse_id, type_of_houses))}\n"
        return self.ussd_continue(menu_text)

        
       
    
