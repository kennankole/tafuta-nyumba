import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

stk_push = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

{    
    "BusinessShortCode":"174379",    
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTYwMjE2MTY1NjI3",    
    "Timestamp":"20160216165627",    
    "TransactionType": "CustomerPayBillOnline",    
    "Amount":"1",    
    "PartyA":"254708374149",    
    "PartyB":"174379",    
    "PhoneNumber":"254708374149",    
    "CallBackURL":"https://mydomain.com/pat",    
    "AccountReference":"Test",    
    "TransactionDesc":"Test"
}


class MpesaC2BCredentials:
    consumer_key = "Er3xIGsMBBtVDuhJ03Ih6YZU4vZGwkMA"
    consumer_secret = "FiKgdP8EbcT7sJpU"
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    
    
class MpesaAccessToken:
    re = requests.get(
        MpesaC2BCredentials.api_url,
        auth=HTTPBasicAuth(MpesaC2BCredentials.consumer_key, MpesaC2BCredentials.consumer_secret)
    )
    mpesa_access_token = re.json()
    validated_mpesa_access_token = mpesa_access_token['access_token']
    

class LipanaMpesaPassword:
    lipa_time = datetime.now().strftime("%Y%m%d%H%M%S")
    business_short_code = "174379"
    password = "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTYwMjE2MTY1NjI3"
  
def get_timestamp():
    unformated_time = datetime.now()
    formated_time = unformated_time.strftime("%Y%m%d%H%M%S")
    return formated_time