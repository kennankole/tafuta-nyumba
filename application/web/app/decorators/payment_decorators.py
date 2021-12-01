import africastalking
from app.config import Config
from app.payment import Mobile
from app.models import CapturingUserData

def charge_users_decorator(func):
    def charge_users_innermost_decorator(self, *args, **kwargs):
        
        charge_users_innermost_decorator.calls += 1
        if charge_users_innermost_decorator.calls >= 3:
            menu_text = "Kindly pay up to continue enjoying our services\n"
            Mobile.checkout("Tafuta-Nyumba", self.phone_number, "KES", 20)
            menu_text += "We are sending you an M-Pesa checkout of KES: 20\n"
            return self.ussd_end(menu_text)
        else:
            return func(self, *args, **kwargs)

    charge_users_innermost_decorator.calls = 0
    return charge_users_innermost_decorator