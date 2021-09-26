from app.menu.base_menu import Menu
from app.business.biz_base_menu import BusinessPremisesMainMenu


class BusinessPremisesQueryMainMenu(BusinessPremisesMainMenu): 
    
    def search_rental_business_premises(self):
        if self.user_response in ("1", "2", "3", "4"):
            menu_text = f"Search business to rent by\n"
            menu_text += "1. Constituency\n2. Ward\n3. City/Town\n"
            self.session['level'] = 110
            self.session['biz_type'] = self.user_response
            return self.ussd_continue(menu_text)

    def search_business_premises_for_sale(self):
        if self.user_response in ("10", "20", "30", "40"):
            menu_text = f"Search business to buy by\n"
            menu_text += "1. Constituency\n2. Ward\n3. City/Town\n"
            self.session['level'] = 110
            self.session['biz_type'] = self.user_response
            return self.ussd_continue(menu_text)

    def register_rental_business_premises(self):
        if self.user_response in ("5", "6", "7", "8"):
            menu_text = f"Register business premises for rent\n"
            menu_text += "1. Yes\n"
            menu_text += "2. No\n"
            self.session['level'] = 110
            self.session['biz_type'] = self.user_response
            return self.ussd_continue(menu_text)

    def register_business_premises_for_sale(self):
        if self.user_response in ("50", "60", "70", "80"):
            menu_text = f"Register business premises for sale\n"
            menu_text += "1. Yes\n"
            menu_text += "2. No\n"
            self.session['level'] = 110
            self.session['biz_type'] = self.user_response
            return self.ussd_continue(menu_text)


    def execute(self):
        level = self.session.get('level')
        menu = {
            11: self.search_rental_business_premises,
            12: self.search_business_premises_for_sale,
            13: self.register_rental_business_premises,
            14: self.register_business_premises_for_sale
        }
        return menu.get(level, self.business_premises_services_menu)()
   