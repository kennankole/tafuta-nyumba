from . menu import HousesQueryMainMenu

class HousesQueryMenu(HousesQueryMainMenu):

    def search_houses_by_location(self):
        if self.user_response == "1":
            menu_text = f"Enter Constituency\n"
            self.session['level'] = 31
            return self.ussd_continue(menu_text)

        if self.user_response == "2":
            menu_text = f"Enter Ward\n "
            self.session['level'] = 32
            return self.ussd_continue(menu_text)

        if self.user_response == "3":
            menu_text = f"Enter Estate or village name\n "
            self.session['level'] = 33
            return self.ussd_continue(menu_text)
        else:
            return self.house_services_menu()


    def execute(self):
        level = self.session.get('level')
        menu = {
            30:self.search_houses_by_location(),
        }
        return menu.get(level, self.house_services_menu)()
            

