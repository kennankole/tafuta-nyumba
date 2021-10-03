from app.menu.menu import LowerLevelMenu

class HostelsMainMenu(LowerLevelMenu):

    def hostels_services_menu(self):
        if self.user_response == "1":
            menu_text = "Search hostels to rent by:\n"
            menu_text += "1. School\n"
            menu_text += "2. Constituency\n"
            menu_text += "3. Ward\n"
            self.session['level'] = 71
            return self.ussd_continue(menu_text)

        if self.user_response == "2":
            menu_text = "Register Hostels\n"
            menu_text += "1. Yes\n"
            menu_text += "2. No\n"
            self.session['level'] = 72
            return self.ussd_continue(menu_text)
        else:
            return self.hostels_menu()

    def execute(self):
        level = self.session.get("level")
        menu = {
            70:self.hostels_services_menu
        }
        return menu.get(level, self.home_menu)()