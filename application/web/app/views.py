import json
import uuid
from flask import Blueprint, g, make_response, request
import africastalking
from app.config import Config
from app import redis

from app.menu.menu import LowerLevelMenu

from app.houses.houses_query_menu import HousesQueryMainMenu
from app.houses.registration import HousesRegistrationMenu
from app.houses.results import HousesQueryResults

from app.hostels.menu import HostelsQueryMenu
from app.hostels.registration import HostelsRegistrationMenu
from app.hostels.results import HostelsQueryResults

from app.business.menu import BusinessPremisesQueryMainMenu
from app.business.registration import BusinessPremisesRegistrationMenu
from app.business.results import BusinessPremisesQueryResults



views = Blueprint("views", __name__)

@views.route("/")
def home_page():
    return 'Welcome to Tafuta Nyumba'


@views.route("/", methods=["POST", "GET"])
def ussd_callback():
    session_id = request.values.get("sessionId") or str(uuid.uuid4())
    service_code = request.values.get("serviceCode")
    phone_number = request.values.get("phoneNumber")
    text = request.values.get("text", "default")
    response = ""
    
    username = Config.USERNAME
    api_key = Config.API_KEY


    africastalking.initialize(username, api_key)
    
    textArray = text.split("*")
    latestInput = textArray[len(textArray) - 2]


    # make this a decorator
    session = redis.get(session_id)
    if session is None:
        session = {'level': 0, 'session_id': session_id}
        redis.set(session_id, json.dumps(session))
    else:
        session = json.loads(session.decode())
    g.user_response = textArray[len(textArray) - 1]
    g.session = session
    g.phone_number = phone_number
    g.session_id = session_id
    # return func(*args, **kwargs)

    level = session.get("level")

    if level < 2:
        menu = LowerLevelMenu(
            session_id=session_id,
            session=g.session,
            phone_number=g.phone_number,
            user_response=g.user_response,
            level=level,
        )
        return menu.execute()

    if level >= 300:
        menu = BusinessPremisesRegistrationMenu(
            session_id=session_id,
            session=g.session,
            phone_number=g.phone_number,
            user_response=g.user_response,
            level=level,
        )
        return menu.execute()

    if level >= 200:
        menu = BusinessPremisesQueryResults(
            session_id=session_id,
            session=g.session,
            phone_number=g.phone_number,
            user_response=g.user_response,
            level=level,
        )
        return menu.execute()

    if level >= 100:
        menu = BusinessPremisesQueryMainMenu(
            session_id=session_id,
            session=g.session,
            phone_number=g.phone_number,
            user_response=g.user_response,
            level=level,
        )
        return menu.execute()

    if level >= 90:
        menu = HostelsRegistrationMenu(
            session_id=session_id,
            session=g.session,
            phone_number=g.phone_number,
            user_response=g.user_response,
            level=level,
        )
        return menu.execute()

    if level >= 80:
        menu = HostelsQueryResults(
            session_id=session_id,
            session=g.session,
            phone_number=g.phone_number,
            user_response=g.user_response,
            level=level,
        )
        return menu.execute()

    if level >= 70:
        menu = HostelsQueryMenu(
            session_id=session_id,
            session=g.session,
            phone_number=g.phone_number,
            user_response=g.user_response,
            level=level,
        )
        return menu.execute()

    if level >= 30:
        menu = HousesRegistrationMenu(
            session_id=session_id,
            session=g.session,
            phone_number=g.phone_number,
            user_response=g.user_response,
            level=level,
        )
        return menu.execute()

    if level >= 20:
        menu = HousesQueryResults(
            session_id=session_id,
            session=g.session,
            phone_number=g.phone_number,
            user_response=g.user_response,
            level=level,
        )
        return menu.execute()

    if level >= 10:
        menu = HousesQueryMainMenu(
            session_id=session_id,
            session=g.session,
            phone_number=g.phone_number,
            user_response=g.user_response,
            level=level,
        )
        return menu.execute()

    else:
        response = make_response("END Ujuzi real estate is out of service\nKind check later")
        response.headers['Content-Type'] = "text/plain"
        return response