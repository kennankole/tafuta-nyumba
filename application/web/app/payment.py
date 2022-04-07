import africastalking
from app.config import Config


class Mobile:
    def __init__(self):
        # Set your app credentials
        self.payment = africastalking.Payment
        self.username = "sandbox"
        self.api_key = Config.API_KEY

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

    @staticmethod
    def checkout():
        product_name = "Tafuta-Nyumba"
        currency_code = "KES"
        phone_number = "+254724747448"
        # phone_number = "+254716244165"
        amount = 10.50

        metadata = {"agentId": "654", "productId": "321"}
        # Get the payments service
        payment = africastalking.Payment
        try:
            res = payment.mobile_checkout(
                product_name, phone_number, currency_code, amount, metadata)
            return res.json
        except Exception as e:
            return f"Received error response: {str(e)}"
        
        
    @staticmethod
    def find_transaction():
        payment = africastalking.Payment
        # Set transaction id to find

        transaction_id = 'ATPid_e95ca121bb7d02cade86868193b91de4'
        # That's it, hit send and we'll take care of the rest
        try:
            res = payment.find_transaction(transaction_id)
            return res
        except Exception as e:
            return "Received error response:%s" % str(e)


class PaymentCheck:
    def __init__(self):
        # Set your app credentials
        self.payment = africastalking.Payment
        self.username = "sandbox"
        self.api_key = Config.API_KEY

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

    
