import json
import os

from app import cache
from decouple import config
from flask import current_app, make_response


class Menu:
    def __init__(
        self, session_id, session, user_response, phone_number=None, level=None
    ):
        self.session_id = session_id
        self.session = session
        self.user_response = user_response
        self.phone_number = phone_number
        self.level = level

    def ussd_continue(self, menu_text):
        cache.set(self.session_id, json.dumps(self.session))
        menu_text = f"CON {menu_text}"
        response = make_response(menu_text, 200)
        response.headers["Content-Type"] = "text/plain"
        return response

    def ussd_end(self, menu_text):
        cache.delete(self.session_id)
        menu_text = f"END {menu_text}"
        response = make_response(menu_text, 200)
        response.headers["Content-Type"] = "text/plain"
        return response

    def home_menu(self):
        menu_text = "Welcome to Tafuta Nyumba\n Choose a service\n"
        menu_text += "1. Houses\n"
        menu_text += "2. Hostels\n"
        menu_text += "3. Business Premises \n"
        self.session["level"] = 1
        self.session["contact"] = self.phone_number
        return self.ussd_continue(menu_text)
