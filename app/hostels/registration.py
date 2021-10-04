from app import db
from app.models import Hostels
from app.menu.base_menu import Menu
class HostelsRegistrationMenu(Menu):

    # @registration_menu_decorator(level=90, message="00.Hostel Registration Menu\n")
    def get_county(self):
        menu_text = "Enter the county\n"
        self.session['level'] = 91
        return self.ussd_continue(menu_text)

    # @location_decorator(level=91, message="Enter the county")
    def get_constituency(self):
        menu_text = "Enter Constituency \n"
        self.session['level'] = 92
        self.session['county'] = self.user_response
        return self.ussd_continue(menu_text)

    # @location_decorator(level=92, message="Enter Constituency \n")
    def get_ward(self):
        menu_text = "Enter Ward \n"
        self.session['level'] = 93
        self.session['constituency'] = self.user_response
        return self.ussd_continue(menu_text)

    # @location_decorator(level=93, message="Enter Ward \n")
    def get_name_of_college_or_univeristy(self):
        menu_text = "Enter name of college or university\n"
        self.session['level'] = 94
        self.session['ward'] = self.user_response
        return self.ussd_continue(menu_text)
    
    # @names_decorator(level=94, message="Enter name of college or university\n")
    def get_units(self):
        menu_text = "Enter units available \n"
        self.session['level'] = 95
        self.session['school_name'] = self.user_response
        return self.ussd_continue(menu_text)

    # @numeric_decorator(level=95, message="Enter units available")
    def get_price(self):
        menu_text = "Enter the price\n"
        self.session['level'] = 96
        self.session['units'] = self.user_response
        return self.ussd_continue(menu_text)
       
    # @numeric_decorator(level=96, message="Enter the price")
    def get_alternate_contact(self):
        menu_text = "Enter alternate contact\n"
        self.session['level'] = 97
        self.session['price'] = self.user_response
        return self.ussd_continue(menu_text)
    
    # @phone_number_decorator(level=97, message="Enter alternate contact")
    def save_data(self):
        menu_text = "Your hostel has been successfully registered\n"
        hostel = Hostels(
            county=self.session.get("county"),
            constituency=self.session.get("constituency"),
            ward=self.session.get("ward"),
            school_name=self.session.get("school_name"),
            units=self.session.get("units"),
            price=self.session.get("price"),
            alternate_contact=self.user_response,
            contacts=self.phone_number
        )
        db.session.add(hostel)
        db.session.commit()
        return self.ussd_end(menu_text)

    def execute(self):
        level = self.session.get('level')

        if level == 90:
            return self.get_county()
        if level == 91:
            return self.get_constituency()
        if level == 92:
            return self.get_ward()
        if level == 93:
            return self.get_name_of_college_or_univeristy()
        if level == 94:
            return self.get_units()
        if level == 95:
            return self.get_price()
        if level == 96:
            return self.get_alternate_contact()
        if level == 97:
            return self.save_data()
