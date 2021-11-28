from app.decorators.location import location_decorator
from app.decorators.names import names_decorator
from app.decorators.payment_decorators import charge_users_decorator
from app.hostels.menu import HostelsQueryMenu
from app.models import Hostels
from app.utils import storing_user_records


class HostelsQueryResults(HostelsQueryMenu):
    @charge_users_decorator
    @names_decorator(level=80, message="Enter name of college or university")
    def hostels_query_results_by_school_name(self):
        storing_user_records(self.phone_number, "renting", "Hostels")
        schl_name = self.user_response
        menu_text = f"Hostels in {schl_name}\n"
        menu_text += f"{Hostels.school_query_results(schl_name=schl_name)}\n"
        menu_text += f"{schl_name.title()} >> (next)\n"
        if Hostels.query.filter_by(school_name=schl_name).count() > 2:
            menu_text = f"Hostels in {schl_name}\n"
            menu_text += "Re-enter school name to see more results\n"
            menu_text += f"{schl_name.title()} >> (next)\n"
            return self.ussd_continue(menu_text)
        
        if 0 < Hostels.query.filter_by(school_name=schl_name).count() <= 2:
            menu_text = f"{str(Hostels.query.filter_by(school_name=schl_name).all())[1:-1]}"
            return self.ussd_end(menu_text)

        else:
            menu_text = "No records\nKindly try again later\n"
            return self.ussd_end(menu_text)
        

    @charge_users_decorator
    @location_decorator(level=81, message="Enter constituency\n")
    def hostels_query_results_by_constituency(self):
        const = self.user_response
        storing_user_records(self.phone_number, "renting", "Hostels")
        if Hostels.query.filter_by(constituency=const).count() > 2:
            menu_text = f"Hostels in {const}\n"
            menu_text += "Re-enter constituency name to see more results\n"
            menu_text += f"{const.title()} >> (next)\n"
            return self.ussd_continue(menu_text)

        if 0 < Hostels.query.filter_by(constituency=const).count() <= 2:
            menu_text = f"{str(Hostels.query.filter_by(constituency=const).all())[1:-1]}"
            return self.ussd_end(menu_text)
        
        else:
            menu_text = "No records\nKindly try again later\n"
            return self.ussd_end(menu_text)
        
        
    @charge_users_decorator
    @location_decorator(level=82, message="Enter ward")
    def hostels_query_results_by_ward(self):
        ward = self.user_response
        storing_user_records(self.phone_number, "renting", "Hostels")
        if Hostels.query.filter_by(ward=ward).count() > 2:
            menu_text = f"Hostels in {ward}\n"
            menu_text += "Re-enter ward name to see more results\n"
            menu_text += f"{ward.title()} >> (next)\n"
            return self.ussd_continue(menu_text)
        
        if 0 < Hostels.query.filter_by(ward=ward).count() <= 2:
            menu_text = f"{str(Hostels.query.filter_by(ward=ward).all())[1:-1]}"
            return self.ussd_end(menu_text)
        
        else:
            menu_text = "No records\nKindly try again later\n"
            return self.ussd_end(menu_text)


    def execute(self):
        level = self.session.get("level")
        menu = {
            80: self.hostels_query_results_by_school_name,
            81: self.hostels_query_results_by_constituency,
            82: self.hostels_query_results_by_ward,
        }
        return menu.get(level, self.hostels_searching_menu)()
