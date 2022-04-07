import requests
from flask import (
    Blueprint, flash, jsonify,
    render_template, request, session,
    url_for, redirect
)
from app.config import Config
from app.revenue.mpesa_auth_token import get_access_token


payment = Blueprint('payment', __name__)

@payment.route("/data", methods=['GET', 'POST'])
def data():
    return request.data
@payment.route('/home', methods=['POST'])
def payment_home():
    return render_template('listing/payment.html')


@payment.route('/lipa/na/mpesa', methods=['POST', 'GET'])
def lipa_na_mpesa_online():
    access_token = get_access_token()
    api_url = Config.STK_PUSH_URL
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": Config.BUSINESS_SHORT_CODE,
        "Password": Config.PASS_KEY,
        "Timestamp": "20220208104429",
        "TransactionType": Config.TRANSACTION_TYPE,
        "Amount": 1, #int(session.get('amount')),
        "PartyA": "254716244165",
        "PartyB": Config.BUSINESS_SHORT_CODE,
        "PhoneNumber": "254716244165",
        "CallBackURL": "https://fad0-196-202-217-18.ngrok.io/lipa/na/mpesa/callback",
        "AccountReference": "Ujuzi.io",
        "TransactionDesc": "Real Estate"
    }
    response = requests.post(api_url, json=request, headers=headers)
    return response.json()

@payment.route("/lipa/online", methods=["POST", "GET"])
def lipa_nyumba_online():
    phone_data = session.get('contacts')
    amount_data = session.get('amount')
    access_token = get_access_token()
    api_url = Config.STK_PUSH_URL
    headers = {"Authorization": "Bearer %s" % access_token}
    if request.method == 'POST':
        phone = request.form['phone']
        amount = request.form['amount']
        
        payload = {
            "BusinessShortCode": Config.BUSINESS_SHORT_CODE,
            "Password": Config.PASS_KEY,
            "Timestamp": "20220208104429",
            "TransactionType": Config.TRANSACTION_TYPE,
            "Amount": amount, 
            "PartyA": phone,
            "PartyB": Config.BUSINESS_SHORT_CODE,
            "PhoneNumber": phone,
            "CallBackURL": "https://4e1e-196-202-217-18.ngrok.io/callback-url",
            "AccountReference": "Ujuzi.io",
            "TransactionDesc": "Real Estate"
        }
        response = requests.post(api_url, json=payload, headers=headers)
        re = response.json()
        try:
            if re['ResponseCode'] == '0':
                flash("Your property has been successfully registered")
                return redirect(url_for('hostels.upload_images'))
        except:
            return redirect(url_for('hostels.hostels_home'))
    return render_template("lipa.html", phone_data=phone_data, amount_data=amount_data)



@payment.route('/callback-url', methods=["POST", "GET"])
def callback_url():
    #get json data set to this route
    json_data = request.get_json()
    #get result code and probably check for transaction success or failure
    result_code = json_data["Body"]["stkCallback"]["ResultCode"]
    message={
        "ResultCode":0,
        "ResultDesc":"success",
        "ThirdPartyTransID":"h234k2h4krhk2"
    }
    #if result code is 0 you can proceed and save the data else if its any other number you can track the transaction
    return jsonify(message), 200


@payment.route('/success', methods=['POST'])
def success():
    return "Your payment has been received!!"

