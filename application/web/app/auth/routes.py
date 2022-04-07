import json
import flask
import requests
from flask import (
    Blueprint, redirect, render_template, request,
    flash, url_for
)
from flask_login import (
    login_required, logout_user, login_user, current_user
)

from app.models import User
from app import db, login_manager, client
from app.config import Config

auth = Blueprint('auth', __name__)

@login_manager.unauthorized_handler
def unauthorized():
    flash('You must be logged in to view that page')
    return redirect(url_for('auth.login'))


# User realestate dashboard
@auth.route('/dashboard')
def dashboard():
    return render_template('auth/dashboard.html')

@auth.route('/here')
def here():
    return f"Hello here "

@auth.route('/there')
def there():
    return f"Hello there "

# Authentication homepage
@auth.route('/index')
def index():
    if current_user.is_authenticated:
        return render_template("auth/account.html")
    return render_template('auth/login.html')

# Google login

# Get the provider configurations
def get_google_provider_cfg():
    '''
    OIDC has a standard endpoint for a provider configuration, which contains a bunch of OAuth 2 and OIDC information. 
    The document with that information is served from a standard endpoint everywhere, ".well-known/openid-configuration".

    Tip: To make this more robust, you should add error handling to the Google API call, 
    just in case Google’s API returns a failure and not the valid provider configuration document.
    This is a function for retrieving Google’s provider configuration:
    '''
    return requests.get(Config.GOOGLE_DISCOVERY_URL).json()

@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    The field from the provider configuration document you need is called 'authorization_endpoint'. 
    This will contain the URL you need to use to initiate the OAuth 2 flow with Google from your client application.

    oauthlib makes the actual request to Google easier. 
        . You use your pre-configured client that you already gave your Google Client ID to. 
        . Next, you provided the redirect you want Google to use. 
        . Finally, you asked Google for a number of OAuth 2 scopes.
    In this case, you’re asking for the user’s email and basic profile information from Google. 

    Note: openid is a required scope to tell Google to initiate the OIDC flow, which will authenticate the user by having them log in. 
    OAuth 2 doesn’t actually standardize how authentication happens, so this is necessary for our flow in this case.

    Once the user logs in with Google and agrees to share their email and basic profile information with your application, 
    Google generates a unique code that it sends back to your application.
    '''
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg['authorization_endpoint']

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=['openid', 'email', 'profile'],
    )
    return redirect(request_uri)

@auth.route('/login/callback', methods=['POST', 'GET'])
def callback():
    '''
    When Google sends back that unique code, it’ll be sending it to this login callback endpoint on your application. 
    The first step is to define the endpoint and get that code:

    The next thing you’re going to do is send that code back to Google’s token endpoint.
    After Google verifies your client credentials, they will send you back tokens that will allow you 
    to authenticate to other Google endpoints on behalf of the user, including the userinfo endpoint. 

    you need to construct the token request. 
    Once the request is constructed, you’ll use the requests library to actually send it out. 
    Then oauthlib, once again, will help you with parsing the tokens from the response:
    '''
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg['token_endpoint']

    # Prepare and send request to get tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(Config.GOOGLE_CLIENT_ID, Config.GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that we have tokens let's find and hit URL
    # from Google that gives you user's profile information,
    # including their Google Profile Image and Email
    userinfo_endpoint = google_provider_cfg['userinfo_endpoint']
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # We want to make sure their email is verified.
    # The user authenticated with Google, authorized our
    # app, and now we've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()['sub']
        users_email = userinfo_response.json()['email']
        picture = userinfo_response.json()['picture']
        users_name = userinfo_response.json()['given_name']
    else:
        return "User email not available or not verified by Google", 400

    user = User(unique_id=unique_id, name=users_name, email=users_email, profile_pic=picture)
    
    if not User.query.filter_by(unique_id=unique_id).first():
        db.session.add(user)
        db.session.commit() 
    login_user(user, force=True, remember=True)
    return redirect(url_for('auth.index'))
    
        
      
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.index'))


@login_manager.user_loader
def user_loader(user_unique_id):
    return User.query.filter_by(unique_id=user_unique_id).first()