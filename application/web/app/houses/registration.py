from app import db
from app.decorators.choices import validate_choices
from app.decorators.location import location_decorator
from app.decorators.payment_decorators import charge_users_decorator
from app.decorators.names import names_decorator
from app.decorators.numeric import numeric_decorator
from app.decorators.phone_numbers import phone_number_decorator
from app.houses.data import houses
from app.houses.utils import get_type_of_house
from app.menu.base_menu import Menu
from app.models import Houses


class HousesRegistrationMenu(Menu):
    def get_registration_consent(self):
        if self.user_response == "1":
            menu_text = "00. House Registration Menu"
            self.session["level"] = 31
            return self.ussd_continue(menu_text)

        if self.user_response == "2":
            menu_text = "Thank you for stopping by\n"
            return self.ussd_end(menu_text)

        if (
            self.user_response not in ("1", "2")
            and self.session.get("sell_house") == "4"
        ):
            menu_text = f"{self.user_response} is an invalid choice\n"
            menu_text += "4. Back\n"
            self.session["level"] = 20
            return self.ussd_continue(menu_text)

        if (
            self.user_response not in ("1", "2")
            and self.session.get("rent_out_house") == "2"
        ):
            menu_text = f"{self.user_response} is an invalid choice\n"
            menu_text += "2. Back\n"
            self.session["level"] = 20
            return self.ussd_continue(menu_text)

    @validate_choices(level=30, message="Invalid Input\n 1/2. Back\n", choices=("00"))
    def get_county(self):
        menu_text = "Enter the county\n"
        self.session["level"] = 32
        return self.ussd_continue(menu_text)

    @location_decorator(level=32, message="Enter the county")
    def get_constituency(self):
        menu_text = "Enter Constituency \n"
        self.session["level"] = 33
        self.session["county"] = self.user_response
        return self.ussd_continue(menu_text)

    @location_decorator(level=33, message="Enter Constituency")
    def get_ward(self):
        menu_text = "Enter Ward \n"
        self.session["level"] = 34
        self.session["constituency"] = self.user_response
        return self.ussd_continue(menu_text)

    @names_decorator(level=35, message="Enter name of the estate")
    def get_estate_village(self):
        menu_text = "Enter name of the estate or village\n"
        self.session["level"] = 35
        self.session["ward"] = self.user_response
        return self.ussd_continue(menu_text)

    @names_decorator(level=35, message="Enter name of the estate")
    def get_house_units(self):
        menu_text = "Enter units available \n"
        self.session["level"] = 36
        self.session["estate_name"] = self.user_response
        return self.ussd_continue(menu_text)

    @numeric_decorator(level=36, message="Enter units available")
    def get_price(self):
        menu_text = "Enter the price\n"
        self.session["level"] = 37
        self.session["units"] = self.user_response
        return self.ussd_continue(menu_text)

    @numeric_decorator(level=37, message="Enter the price")
    def get_alternate_contacts(self):
        menu_text = "Enter an alternative phone number\n"
        self.session["level"] = 38
        self.session["price"] = self.user_response
        return self.ussd_continue(menu_text)

    # @charge_users_decorator
    @phone_number_decorator(level=38, message="Enter an alternative phone number")
    def save_data(self):
        units = self.session.get("units")
        price = self.session.get("price")
        chargeable_amount = (0.05 * int(price) * int(units))
        for_rent = bool
        house = get_type_of_house(self.session.get("hse_type"), houses)
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
            type_of_house=get_type_of_house(self.session.get("hse_type"), houses),
            for_rent=for_rent,
            alternate_contact=self.user_response,
            contacts=self.phone_number,
        )
        db.session.add(house)
        db.session.commit()
        menu_text = f"To complete your registration, we are sending you an M-Pesa checkout of {chargeable_amount}\nValue at 5% per unit price\n"
        menu_text += f"Your {get_type_of_house(self.session.get('hse_type'), houses)} have been successfully registered\n"
        return self.ussd_end(menu_text)

    def execute(self):
        level = self.session.get("level")

        if level == 30:
            return self.get_registration_consent()
        if level == 31:
            return self.get_county()
        if level == 32:
            return self.get_constituency()
        if level == 33:
            return self.get_ward()
        if level == 34:
            return self.get_estate_village()
        if level == 35:
            return self.get_house_units()
        if level == 36:
            return self.get_price()
        if level == 37:
            return self.get_alternate_contacts()
        if level == 38:
            return self.save_data()
