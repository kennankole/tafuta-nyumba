from flask import Blueprint

views = Blueprint("views", __name__)

@views.route("/")
def home_page():
    return 'Welcome to Tafuta Nyumba'