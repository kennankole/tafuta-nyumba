from pyexpat import model
from flask import Blueprint, render_template
from app import models


home = Blueprint('home', __name__)


@home.route('/listing/home', methods=['GET', 'POST'])
def home_page():
    hostels_ = models.Hostels().get_all__hostel_coordinates_to_geojson()
    return render_template("maps/home_page.html", hostels=hostels_)
    