from app.houses.houses_base_menu import HousesMainMenu
from app.houses import data
from app.houses.utils import get_type_of_house

from app.decorators.choices import validate_choices


class HousesQueryMainMenu(HousesMainMenu):
    @validate_choices(
        level=10,
        message="Invalid Entry\n1. Back",
        choices=("1", "2", "3", "4", "5", "6"),
    )
    def search_houses_to_rent_by_location(self):
        # if self.user_response in ("1", "2", "3", "4", "5", "6"):
        house = get_type_of_house(self.user_response, data.houses)
        menu_text = f"Search {house} to rent by no.{self.user_response}:\n"
        menu_text += "1. Constituency\n2. Ward\n3. Estate or Village\n"
        self.session["level"] = 20
        self.session["hse_type"] = self.user_response
        return self.ussd_continue(menu_text)

    @validate_choices(level=10, message="3. Back\n", choices=("10", "20", "30", "40"))
    def search_houses_to_buy_by_location(self):
        # if self.user_response in ("10", "20", "30", "40"):
        house = get_type_of_house(self.user_response, data.houses)
        menu_text = f"Search {house} to buy by:\n"
        menu_text += "1. Constituency\n2. Ward\n3. Estate or Village\n"
        self.session["level"] = 20
        self.session["hse_type"] = self.user_response
        return self.ussd_continue(menu_text)

    @validate_choices(
        level=10, message="2. Back\n", choices=("11", "12", "13", "14", "15", "16")
    )
    def rental_houses_registration(self):
        house = get_type_of_house(self.user_response, data.houses)
        # if self.user_response in ("11", "12", "13", "14", "15", "16"):
        menu_text = f"Register {house} for rent\n"
        menu_text += "1. Yes\n"
        menu_text += "2. No\n"
        self.session["level"] = 30
        self.session["hse_type"] = self.user_response
        return self.ussd_continue(menu_text)

    @validate_choices(level=10, message="2. Back\n", choices=("50", "60", "70", "80"))
    def register_houses_for_sale(self):
        house = get_type_of_house(self.user_response, data.houses)
        # if self.user_response in ("50", "60", "70", "80"):
        menu_text = f"Register {house} for sale\n"
        menu_text += "1. Yes\n"
        menu_text += "2. No\n"
        self.session["level"] = 30
        self.session["hse_type"] = self.user_response
        return self.ussd_continue(menu_text)

    def execute(self):
        level = self.session.get("level")
        menu = {
            11: self.search_houses_to_rent_by_location,
            12: self.search_houses_to_buy_by_location,
            13: self.rental_houses_registration,
            14: self.register_houses_for_sale,
        }
        return menu.get(level, self.house_services_menu)()
