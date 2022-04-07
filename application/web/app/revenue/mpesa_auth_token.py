import requests
import json
from requests.auth import HTTPBasicAuth
from app.config import Config

def get_access_token():
    consumer_key = Config.CONSUMER_KEY
    consumer_secret = Config.CONSUMER_SECRET
    api_url = Config.API_URL
    re = requests.get(api_url, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(re.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    return validated_mpesa_access_token


