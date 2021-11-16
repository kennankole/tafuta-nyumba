from app import db
from app.business.data import types_of_business_premises
from app.business.utils import get_type_of_business_premises
from app.decorators.choices import validate_choices
from app.decorators.location import location_decorator
from app.decorators.names import names_decorator
from app.decorators.numeric import numeric_decorator
from app.decorators.phone_numbers import phone_number_decorator
from app.menu.base_menu import Menu
from app.models import BusinessPremises


class BusinessPremisesRegistrationMenu(Menu):
    def get_registration_consent(self):
        if self.user_response == "1":
            menu_text = "00. Business Registration Menu"
            self.session["level"] = 301
            return self.ussd_continue(menu_text)

        elif self.user_response == "2":
            menu_text = "Thank you for stopping by\n"
            return self.ussd_end(menu_text)

        elif (
            self.user_response not in ("1", "2")
            and self.session.get("sell_business") == "4"
        ):
            menu_text = f"{self.user_response} is an invalid choice\n"
            menu_text += "4. Back\n"
            self.session["level"] = 100
            return self.ussd_continue(menu_text)

        elif (
            self.user_response not in ("1", "2")
            and self.session.get("rent_out_business") == "2"
        ):
            menu_text = f"{self.user_response} is an invalid choice\n"
            menu_text += "2. Back\n"
            self.session["level"] = 100
            return self.ussd_continue(menu_text)
        else:
            menu_text = "is an invalid selection!!\n"
            menu_text += f"{self.session.get('rent_out_business'), self.session.get('sell_business')}"
            return self.ussd_continue(menu_text)

    @validate_choices(level=300, message="Invalid Input\n1. Back\n", choices=("00"))
    def get_county(self):
        menu_text = "Enter the county\n"
        self.session["level"] = 302
        return self.ussd_continue(menu_text)

    @location_decorator(level=302, message="Enter the county")
    def get_constituency(self):
        menu_text = "Enter Constituency \n"
        self.session["level"] = 303
        self.session["county"] = self.user_response
        return self.ussd_continue(menu_text)

    @location_decorator(level=303, message="Enter Constituency")
    def get_ward(self):
        menu_text = "Enter Ward \n"
        self.session["level"] = 304
        self.session["constituency"] = self.user_response
        return self.ussd_continue(menu_text)

    @location_decorator(level=304, message="Enter Ward \n")
    def get_town_or_city_name(self):
        menu_text = "Enter name of the town or city\n"
        self.session["level"] = 305
        self.session["ward"] = self.user_response
        return self.ussd_continue(menu_text)

    @names_decorator(
        level=305, message="Invalid input\nEnter name of the town or city\n"
    )
    def get_street_name(self):
        menu_text = "Enter the street name \n"
        self.session["level"] = 306
        self.session["name_of_city"] = self.user_response
        return self.ussd_continue(menu_text)

    @names_decorator(
        level=306, message="Invalid input\nEnter name of the town or city\n"
    )
    def get_biz_premises_units(self):
        menu_text = "Enter units available \n"
        self.session["level"] = 307
        self.session["street_name"] = self.user_response
        return self.ussd_continue(menu_text)

    @numeric_decorator(level=307, message="Enter units available")
    def get_biz_premises_floor_area(self):
        menu_text = "Enter the floor area\n"
        self.session["level"] = 308
        self.session["biz_premises_units"] = self.user_response
        return self.ussd_continue(menu_text)

    @numeric_decorator(level=308, message="Enter floor area in square feet")
    def get_price(self):
        menu_text = "Enter the price\n"
        self.session["level"] = 309
        self.session["biz_floor_area"] = self.user_response
        return self.ussd_continue(menu_text)

    @numeric_decorator(level=309, message="Enter the price")
    def get_alternate_contacts(self):
        menu_text = "Enter an alternative phone number\n"
        self.session["level"] = 400
        self.session["price"] = self.user_response
        return self.ussd_continue(menu_text)

    @phone_number_decorator(level=309, message="Enter alternate contact")
    def save_data(self):
        for_rent = False
        biz_premises = get_type_of_business_premises(
            self.session.get("biz_type"), types_of_business_premises
        )
        menu_text = f"Your {biz_premises} have been successfully registered\n"
        if self.session.get("rent_out_biz_premises"):
            for_rent = True
        if self.session.get("sell_business"):
            for_rent = False
        biz_premises = BusinessPremises(
            county=self.session.get("county"),
            constituency=self.session.get("constituency"),
            ward=self.session.get("ward"),
            name_of_city_or_town=self.session.get("name_of_city"),
            street_name=self.session.get("street_name"),
            units=self.session.get("biz_premises_units"),
            price=self.session.get("price"),
            area=self.session.get("biz_floor_area"),
            type_of_business_premise=get_type_of_business_premises(
                self.session.get("biz_type"), types_of_business_premises
            ),
            for_rent=for_rent,
            alternate_contact=self.user_response,
            contacts=self.phone_number,
        )
        db.session.add(biz_premises)
        db.session.commit()
        return self.ussd_end(menu_text)

    def execute(self):
        level = self.session.get("level")

        if level == 300:
            return self.get_registration_consent()
        if level == 301:
            return self.get_county()
        if level == 302:
            return self.get_constituency()
        if level == 303:
            return self.get_ward()
        if level == 304:
            return self.get_town_or_city_name()
        if level == 305:
            return self.get_street_name()
        if level == 306:
            return self.get_biz_premises_units()
        if level == 307:
            return self.get_biz_premises_floor_area()
        if level == 308:
            return self.get_price()
        if level == 309:
            return self.get_alternate_contacts()
        if level == 400:
            return self.save_data()
