from app.decorators.choices import validate_choices

from .hostels_base_menu import HostelsMainMenu


class HostelsQueryMenu(HostelsMainMenu):
    @validate_choices(
        level=70, message="Invalid Entry\n1. Back", choices=("1", "2", "3")
    )
    def hostels_searching_menu(self):
        if self.user_response == "1":
            menu_text = "Enter name of college or university \n"
            self.session["level"] = 80
            return self.ussd_continue(menu_text)

        if self.user_response == "2":
            menu_text = "Enter constituency\n"
            self.session["level"] = 81
            return self.ussd_continue(menu_text)

        if self.user_response == "3":
            menu_text = "Enter ward\n"
            self.session["level"] = 82
            return self.ussd_continue(menu_text)

        else:
            return self.hostels_services_menu()

    def execute(self):
        level = self.session.get("level")
        menu = {
            71: self.hostels_searching_menu,
        }
        return menu.get(level, self.hostels_services_menu)()
