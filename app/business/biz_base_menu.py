from app.menu.menu import LowerLevelMenu

class BusinessPremisesMainMenu(LowerLevelMenu):

    def business_premises_services_menu(self):
        if self.user_response == "1":
            menu_text = f"Select type of business premise to rent\n"
            menu_text += "1. Kiosk/Kibanda\n"
            menu_text += "2. Shops\n"
            menu_text += "3. Office Space\n"
            menu_text += "4. Go-Downs\n"
            self.session['rent_business'] = self.user_response
            self.session['level'] = 301 
            return self.ussd_continue(menu_text)

        if self.user_response == "2":
            menu_text = f"Select type of business premise to rent out\n"
            menu_text += "5. Kiosk/Kibanda\n"
            menu_text += "6. Shops\n"
            menu_text += "7. Office Space\n"
            menu_text += "8. Go-Downs\n"
            self.session['rent_out_business'] = self.user_response
            self.session['level'] = 303
            return self.ussd_continue(menu_text)

        if self.user_response == "3":
            menu_text = f"Select type of business premise to buy\n"
            menu_text += "10. Kiosk/Kibanda\n"
            menu_text += "20. Shops\n"
            menu_text += "30. Office Space\n"
            menu_text += "40. Go-Downs\n"
            self.session['level'] = 302
            self.session['buy_business'] = self.user_response
            return self.ussd_continue(menu_text)

        if self.user_response == "4":
            menu_text = f"Select type of business premise to sell\n"
            menu_text += "50. Kiosk/Kibanda\n"
            menu_text += "60. Shops\n"
            menu_text += "70. Office Space\n"
            menu_text += "80 Go-Downs\n"
            self.session['level'] = 304
            self.session['sell_business'] = self.user_response
            return self.ussd_continue(menu_text)
        else:
           return self.business_premises_menu()