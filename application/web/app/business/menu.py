from app.business.biz_base_menu import BusinessPremisesMainMenu
from app.decorators.choices import validate_choices


class BusinessPremisesQueryMainMenu(BusinessPremisesMainMenu):
    @validate_choices(level=100, message="1. Back", choices=("1", "2", "3", "4"))
    def search_rental_business_premises(self):
        if self.user_response in ("1", "2", "3", "4"):
            menu_text = "Search business to rent by\n"
            menu_text += "1. Name of city\n2. Constituency\n3. Ward\n"
            self.session["level"] = 200
            self.session["biz_type"] = self.user_response
            return self.ussd_continue(menu_text)

    @validate_choices(level=100, message="2. Back", choices=("5", "6", "7", "8"))
    def register_rental_business_premises(self):
        if self.user_response in ("5", "6", "7", "8"):
            menu_text = "Register business premises for rent\n"
            menu_text += "1. Yes\n"
            menu_text += "2. No\n"
            self.session["level"] = 300
            self.session["biz_type"] = self.user_response
            return self.ussd_continue(menu_text)

    @validate_choices(level=100, message="3. Back", choices=("10", "20", "30", "40"))
    def search_business_premises_for_sale(self):
        if self.user_response in ("10", "20", "30", "40"):
            menu_text = "Search business to buy by\n"
            menu_text += "1. Name of city\n2. Constituency\n3. Ward\n"
            self.session["level"] = 200
            self.session["biz_type"] = self.user_response
            return self.ussd_continue(menu_text)

    @validate_choices(level=100, message="4. Back", choices=("50", "60", "70", "80"))
    def register_business_premises_for_sale(self):
        if self.user_response in ("50", "60", "70", "80"):
            menu_text = "Register business premises for sale\n"
            menu_text += "1. Yes\n"
            menu_text += "2. No\n"
            self.session["level"] = 300
            self.session["biz_type"] = self.user_response
            return self.ussd_continue(menu_text)

    def execute(self):
        level = self.session.get("level")
        menu = {
            101: self.search_rental_business_premises,
            102: self.register_rental_business_premises,
            103: self.search_business_premises_for_sale,
            104: self.register_business_premises_for_sale,
        }
        return menu.get(level, self.business_premises_services_menu)()
