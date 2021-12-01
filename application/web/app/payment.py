import africastalking
from app.config import Config

class Mobile:
    def __init__(self):
        self.payment = africastalking.Payment
        self.username = "sandbox"
        self.api_key = Config.API_KEY

        africastalking.initialize(self.username, self.api_key)
        
    @classmethod
    def checkout(product_name, phone_number, currency_code, amount):
        metadata = {"agentId" : "654", "productId" : "321"}
        payment = africastalking.Payment
        try:
            res = payment.mobile_checkout(product_name=product_name, phone_number=phone_number, currency_code=currency_code, amount=amount, metadata=metadata)
            return res
        except Exception as e:
            return f"Received error response: {str(e)}"
