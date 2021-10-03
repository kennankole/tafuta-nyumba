from . hostels_base_menu import HostelsMainMenu

class HostelsQueryMenu(HostelsMainMenu):

    def hostels_searching_menu(self):
        if self.user_response == "1":
            menu_text = "Enter name of college or university \n"
            self.session['level'] = 80
            return self.ussd_continue(menu_text)

        if self.user_response == "2":
            menu_text = "Enter constituency\n"
            self.session['level'] = 81
            return self.ussd_continue(menu_text)

        if self.user_response == "3":
            menu_text = "Enter ward\n"
            self.session['level'] = 82
            return self.ussd_continue(menu_text)

        else:
            return self.hostels_services_menu()

    def hostels_registration_menu(self):
        if self.user_response == "1":
            menu_text = "00. Hostel Registration Menu\n"
            self.session['level'] = 90
            return self.ussd_continue(menu_text)

        if self.user_response == "2":
            menu_text = "Thank you for stopping by\n"
            return self.ussd_end(menu_text)
        else:
            menu_text = f"{self.user_response} is an invalid selection!!\n"
            menu_text += "2. Back\n"
            self.session['level'] = 70
            return self.ussd_continue(menu_text)

    def execute(self):
        level = self.session.get("level")
        menu = {
            71:self.hostels_searching_menu,
            72:self.hostels_registration_menu
        }
        return menu.get(level, self.hostels_services_menu)()

        