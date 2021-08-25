from app.menu.menu import LowerLevelMenu

class HousesMainMenu(LowerLevelMenu):
    
    def house_services_menu(self):
        if self.user_response == "1":
            menu_text = f"Select type of house to rent\n"
            menu_text += "1. Single room\n"
            menu_text += "2. Double room\n"
            menu_text += "3. Bedsitter\n"
            menu_text += "4. One Bedroom\n"
            menu_text += "5. Two Bedroom\n"
            menu_text += "6. Three Bedroom\n"
            self.session['level'] = 11 
            self.session['rent_house'] = self.user_response
            return self.ussd_continue(menu_text)

        if self.user_response == "2":
            menu_text = f"Select type of house to rent out\n"
            menu_text += "11. Single room\n"
            menu_text += "12. Double room\n"
            menu_text += "13. Bedsitter\n"
            menu_text += "14. One Bedroom\n"
            menu_text += "15. Two Bedroom\n"
            menu_text += "16. Three Bedroom\n"
            self.session['level'] = 13
            self.session['rent_out_house'] = self.user_response
            return self.ussd_continue(menu_text)

        if self.user_response == "3":
            menu_text = f"Select type of house to buy\n"
            menu_text += "10. Bedsitter\n"
            menu_text += "20. One Bedroom\n"
            menu_text += "30. Two Bedroom\n"
            menu_text += "40. Three Bedroom\n"
            self.session['level'] = 12
            self.session['buy_house'] = self.user_response
            return self.ussd_continue(menu_text)

        if self.user_response == "4":
            menu_text = f"Select type of house to sell\n"
            menu_text += "50. Bedsitter\n"
            menu_text += "60. One Bedroom\n"
            menu_text += "70. Two Bedroom\n"
            menu_text += "80. Three Bedroom\n"
            self.session['level'] = 14
            self.session['sell_house'] = self.user_response
            return self.ussd_continue(menu_text)
        else:
           return self.house_menu()

    def execute(self):
        level = self.session.get('level')
        menu = {
           10:self.house_services_menu()
        }
        return menu.get(level, self.home_menu)()