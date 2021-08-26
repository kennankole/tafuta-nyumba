from app.menu.base_menu import Menu
from app import db
from app.models  import Houses
from app.houses.data import type_of_houses
from . utils import get_type_of_house

class HousesRegistrationMenu(Menu):

    def get_registration_consent(self):
        if self.user_response == "1":
            menu_text = "00. House Registration Menu"
            self.session['level'] = 31
            return self.ussd_continue(menu_text)

        if self.user_response == "2":
            menu_text = "Thank you for stopping by\n"
            return self.ussd_end(menu_text)

        if self.user_response not in ("1", "2") and self.session.get("sell_house") == "4":
            menu_text = f"{self.user_response} is an invalid choice\n"
            menu_text += "4. Back\n"
            self.session['level'] = 20
            return self.ussd_continue(menu_text)

        if self.user_response not in ("1", "2") and self.session.get("rent_out_house") == "2":
            menu_text = f"{self.user_response} is an invalid choice\n"
            menu_text += "2. Back\n"
            self.session['level'] = 20
            return self.ussd_continue(menu_text)


    def get_county(self):
        menu_text = "Enter the county\n"
        self.session['level'] = 32 
        return self.ussd_continue(menu_text)

    def get_constituency(self):
        menu_text = "Enter Constituency \n"
        self.session['level'] = 33
        self.session['county'] = self.user_response
        return self.ussd_continue(menu_text)

    def get_ward(self):
        menu_text = "Enter Ward \n"
        self.session['level'] = 34
        self.session['constituency'] = self.user_response
        return self.ussd_continue(menu_text)

    def get_estate_village(self):
        menu_text = "Enter name of the estate or village\n"
        self.session['level'] = 35
        self.session['ward'] = self.user_response
        return self.ussd_continue(menu_text)

    def get_house_units(self):
        menu_text = "Enter units available \n"
        self.session['level'] = 36
        self.session['estate_name'] = self.user_response
        return self.ussd_continue(menu_text)

    def get_price(self):
        menu_text = "Enter the price\n"
        self.session['level'] = 37
        self.session['units'] = self.user_response
        return self.ussd_continue(menu_text)
    
    def get_alternate_contacts(self):
        menu_text = "Enter an alternative phone number\n"
        self.session['level'] = 38
        self.session['price'] = self.user_response
        return self.ussd_continue(menu_text)


    def save_data(self):
        house = get_type_of_house(self.session.get('hse_type'), type_of_houses)
        menu_text = f"Your {house}(s) have been successfully registered\n"
        if self.session.get("rent_out_house"):
            for_rent = True
        if self.session.get("sell_house"):
            for_rent = False
        house = Houses(
            county=self.session.get("county"),
            constituency=self.session.get("constituency"),
            ward=self.session.get("ward"),
            name_of_estate_or_village=self.session.get("estate_name"),
            units=self.session.get("units"),
            price=self.session.get("price"),
            type_of_house=get_type_of_house(self.session.get('hse_type'), type_of_houses),
            for_rent=for_rent,
            alternate_contact=self.user_response,
            contacts=self.phone_number
        )
        db.session.add(house)
        db.session.commit()
        return self.ussd_end(menu_text)



    