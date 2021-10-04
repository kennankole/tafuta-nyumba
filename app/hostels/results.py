from . menu import HostelsQueryMenu
from app.hostels.menu import HostelsQueryMenu
from app.models import Hostels

class HostelsQueryResults(HostelsQueryMenu):

    # @charge_users_decorator
    # @names_decorator(level=80, message="Enter name of college or university")
    def hostels_query_results_by_school_name(self):
        # storing_user_records(self.phone_number, "renting", "Hostels")
        schl_name = self.user_response
        menu_text = f"Hostels in {schl_name}\n"
        if not Hostels.query.filter_by(school_name=schl_name).first():
            menu_text = f"No hostels in {schl_name}\nKindly check later\n"
            return self.ussd_end(menu_text)
        else:
            menu_text = f"{Hostels.hostels_results(school_name=schl_name)}\n"
            menu_text += f"{schl_name.title()} >> (next)\n"
            return self.ussd_continue(menu_text)

    # @charge_users_decorator
    # @location_decorator(level=81, message="Enter constituency\n")
    def hostels_query_results_by_constituency(self):
        # storing_user_records(self.phone_number, "renting", "Hostels")
        const = self.user_response
        if not Hostels.query.filter_by(constituency=const).first():
            menu_text = f"No hostels in {const}\nKindly check later.\n"
            return self.ussd_end(menu_text)
        else:
            menu_text = f"{Hostels.constituency_results(const=const)}\n"
            menu_text = f"{const.title()} >> (next)\n"
            return self.ussd_continue(menu_text)

    # @charge_users_decorator
    # @location_decorator(level=82, message="Enter ward")
    def hostels_query_results_by_ward(self):
        # storing_user_records(self.phone_number, "renting", "Hostels")
        ward = self.user_response
        if not Hostels.query.filter_by(ward=ward).first():
            menu_text = f"No hostels in {ward}\nKindly check later.\n"
            return self.ussd_end(menu_text)
        else:
            menu_text = f"{Hostels.ward_results(ward=ward)}\n"
            menu_text = f"{ward.title()} >> (next)\n"
            return self.ussd_continue(menu_text)
    
    def execute(self):
        level = self.session.get('level')
        menu = {
            80: self.hostels_query_results_by_school_name,
            81: self.hostels_query_results_by_constituency,
            82: self.hostels_query_results_by_ward
        }
        return menu.get(level, self.hostels_searching_menu)()