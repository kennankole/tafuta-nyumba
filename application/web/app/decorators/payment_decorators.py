import africastalking
from africastalking import Payment
from app.config import Config
from app.models import CapturingUserData

def charge_users_decorator(func):
    def charge_users_innermost_decorator(self, *args, **kwargs):
        
        charge_users_innermost_decorator.calls += 1
        if charge_users_innermost_decorator.calls >= 3:
            payment = africastalking.Payment
            menu_text = "Kindly pay up to continue enjoying our services\n"
            payment.mobile_checkout(productName="Tafuta-Nyumba", phoneNumber=self.phone_number, currencyCode="KES", amount=20)
            menu_text += "We are sending you an M-Pesa checkout of KES: 20\n"
            return self.ussd_end(menu_text)
        else:
            return func(self, *args, **kwargs)

    charge_users_innermost_decorator.calls = 0
    return charge_users_innermost_decorator