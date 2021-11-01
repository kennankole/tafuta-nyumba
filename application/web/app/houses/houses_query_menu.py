from .menu import HousesQueryMainMenu
from app.decorators.choices import validate_choices


class HousesQueryMenu(HousesQueryMainMenu):
    @validate_choices(
        level=10, message="Invalid Entryy\n 1. Back", choices=("1", "2", "3")
    )
    def search_houses_by_location(self):
        if self.user_response == "1":
            menu_text = "Enter Constituency\n"
            self.session["level"] = 21
            return self.ussd_continue(menu_text)

        if self.user_response == "2":
            menu_text = "Enter Ward\n "
            self.session["level"] = 22
            return self.ussd_continue(menu_text)

        if self.user_response == "3":
            menu_text = "Enter Estate or village name\n "
            self.session["level"] = 23
            return self.ussd_continue(menu_text)
        # else:
        #     menu_text = "Hey\n"
        #     return self.ussd_end(menu_text)

    def execute(self):
        level = self.session.get("level")
        menu = {
            20: self.search_houses_by_location(),
        }
        return menu.get(level, self.house_services_menu)()
