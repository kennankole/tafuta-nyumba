from app.menu.base_menu import Menu

class LowerLevelMenu(Menu):
    
    def house_menu(self):
        menu_text = "Select Houses to;\n"
        menu_text += "1. Rent \n2. Rent out\n3. Buy\n4. Sell \n"
        self.session['level'] = 10
        return self.ussd_continue(menu_text)

    def hostels_menu(self):
        menu_text = "Select Hostels to;\n"
        menu_text += "1. Rent \n2. Rent out\n"
        self.session['level'] = 70
        return self.ussd_continue(menu_text)

    def business_premises_menu(self):
        menu_text = "Select Business Premises to;\n"
        menu_text += "1. Rent \n2. Rent out \n3. Buy \n4. Sell \n"
        self.session['level'] = 100
        return self.ussd_continue(menu_text)

    
    def execute(self):
        menu = {
            "1": self.house_menu,
            "2": self.hostels_menu,
            "3": self.business_premises_menu
        }
        return menu.get(self.user_response, self.home_menu)()
       