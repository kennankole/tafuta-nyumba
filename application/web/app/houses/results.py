from app.decorators.location import location_decorator
from app.decorators.names import names_decorator
from app.decorators.payment_decorators import charge_users_decorator
from app.houses.data import houses
from app.houses.houses_query_menu import HousesQueryMenu
from app.houses.utils import get_type_of_house
from app.models import Houses

# from app.utils import storing_user_records



class HousesQueryResults(HousesQueryMenu):
    @charge_users_decorator
    @location_decorator(level=21, message="Enter Constituency Really")
    def houses_const_query_results(self):
        rent = True
        hse_id = self.session.get("hse_type")
        const = self.user_response
        if self.session.get("rent_house"):
            rent = True
            service_type = "renting"
        if self.session.get("buy_house"):
            rent = False
            service_type = "buying"
        # storing_user_records(self.phone_number, service_type,get_type_of_house(houses, hse_id))
        menu_text = f"{get_type_of_house(hse_id, houses)} in {const}\n"
        menu_text += f"{Houses.constituency_results(const=const, rent=rent, hse_type=get_type_of_house(hse_id, houses))}\n"
        return self.ussd_continue(menu_text)

    @charge_users_decorator
    @location_decorator(level=22, message="Enter Ward")
    # @names_decorator(level=22, message="Enter ward")
    def houses_ward_query_results(self):
        rent = True
        # service_type = ""
        hse_id = self.session.get("hse_type")
        ward = self.user_response
        if self.session.get("rent_house"):
            rent = True
            service_type = "renting"
        if self.session.get("buy_house"):
            rent = False
            # service_type = "buying"
        # storing_user_records(self.phone_number, service_type,get_type_of_house(houses, hse_id))
        menu_text = f"{get_type_of_house(hse_id, houses)} in {ward}\n"
        menu_text += f"{Houses.ward_results(ward=ward, rent=rent, hse_type=get_type_of_house(hse_id, houses))}\n"
        return self.ussd_continue(menu_text)

    @charge_users_decorator
    @names_decorator(level=23, message="Enter Estate or village name")
    def houses_village_estate_query_results(self):
        # rent = True
        hse_id = self.session.get("hse_type")
        village_estate = self.user_response
        if self.session.get("rent_house"):
            rent = True
            # service_type = "renting"
        if self.session.get("buy_house"):
            rent = False
            # service_type = "buying"
        # storing_user_records(self.phone_number, service_type,get_type_of_house(houses, hse_id))
        menu_text = f"{get_type_of_house(hse_id, houses)} in {village_estate}\n"
        menu_text += f"{Houses.village_estate_results(village_estate=village_estate, rent=rent, hse_type=get_type_of_house(hse_id, houses))}\n"
        return self.ussd_continue(menu_text)

    def execute(self):
        level = self.session.get("level")
        menu = {
            21: self.houses_const_query_results,
            22: self.houses_ward_query_results,
            23: self.houses_village_estate_query_results,
        }
        return menu.get(level, self.search_houses_by_location)()
