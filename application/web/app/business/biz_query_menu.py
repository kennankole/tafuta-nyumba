from app.decorators.choices import validate_choices

from .menu import BusinessPremisesQueryMainMenu


class BusinessPremisesQueryMenu(BusinessPremisesQueryMainMenu):
    @validate_choices(
        level=100, message="Invalid Entry\n 1. Back", choices=("1", "2", "3")
    )
    def search_business_premises_by_location(self):
        if self.user_response == "1":
            menu_text = "Enter name of city\n"
            self.session["level"] = 201
            return self.ussd_continue(menu_text)

        if self.user_response == "2":
            menu_text = "Enter Constituency\n "
            self.session["level"] = 202
            return self.ussd_continue(menu_text)

        if self.user_response == "3":
            menu_text = "Enter Ward\n "
            self.session["level"] = 203
            return self.ussd_continue(menu_text)
        else:
            return self.business_premises_services_menu()

    def execute(self):
        level = self.session.get("level")
        menu = {
            200: self.search_business_premises_by_location,
        }
        return menu.get(level, self.business_premises_services_menu)()
