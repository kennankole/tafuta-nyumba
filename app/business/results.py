from app.business.biz_query_menu import BusinessPremisesQueryMenu
from app.models import BusinessPremises
from app.business.data import types_of_business_premises
from app.business.utils import get_type_of_business_premises


class BusinessPremisesQueryResults(BusinessPremisesQueryMenu):

    def biz_premises_const_query_results(self):
        rent = True
        biz_id = self.session.get("biz_type")
        const = self.user_response
        if self.session.get("rent_business"):
            rent = True
            service_type = "renting"
        if self.session.get("buy_business"):
            rent = False
            service_type = "buying"
        # storing_user_records(self.phone_number, service_type,get_type_of_business_premises(type_of_biz_premises, biz_id)) 
        menu_text = f"{get_type_of_business_premises(biz_id, types_of_business_premises)} in {const}\n"
        menu_text += f"{BusinessPremises.constituency_results(const=const, rent=rent, biz_type=get_type_of_business_premises(biz_id, types_of_business_premises))}\n"
        return self.ussd_continue(menu_text)


    def biz_premises_ward_query_results(self):
        rent = True
        biz_id = self.session.get('biz_type')
        ward = self.user_response
        if self.session.get("rent_business"):
            rent = True
            service_type = "renting"
        if self.session.get("buy_business"):
            rent = False
            service_type = "buying"
        # storing_user_records(self.phone_number, service_type,get_type_of_business_premises(type_of_biz_premises, biz_id)) 
        menu_text = f"{get_type_of_business_premises(biz_id, types_of_business_premises)} in {ward}\n"
        menu_text += f"{BusinessPremises.ward_results(ward=ward, rent=rent, biz_type=get_type_of_business_premises(biz_id, types_of_business_premises))}\n"
        return self.ussd_continue(menu_text)

    def biz_premises_city_or_town_results(self):
        rent = True
        biz_id = self.session.get('biz_type')
        city_or_town = self.user_response
        if self.session.get("rent_business"):
            rent = True
            service_type = "renting"
        if self.session.get("buy_business"):
            rent = False
            service_type = "buying"
        # storing_user_records(self.phone_number, service_type,get_type_of_business_premises(type_of_biz_premises, biz_id)) 
        menu_text = f"{get_type_of_business_premises(biz_id, types_of_business_premises)} in {city_or_town}\n"
        menu_text += f"{BusinessPremises.city_or_town_results(city_or_town=city_or_town, rent=rent, biz_type=get_type_of_business_premises(biz_id, types_of_business_premises))}\n"
        return self.ussd_continue(menu_text)

    def execute(self):
        level = self.session.get('level')
        menu = {
            21: self.biz_premises_const_query_results,
            22: self.biz_premises_ward_query_results,
            23: self.biz_premises_city_or_town_results
        }
        return menu.get(level, self.search_business_premises_by_location)()


        
       
    
