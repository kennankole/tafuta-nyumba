import imp
from flask import Blueprint, url_for, render_template
from app import models 

dashboard = Blueprint("dashboard", __name__)

@dashboard.route('/admin', methods=['POST', 'GET'])
def dashboard_page():
    houses = models.Houses.query.all()
    hostels = models.Hostels.query.all()
    businesses = models.BusinessPremises.query.all()
    
    return render_template(
        'dashboard/index.html', 
        houses=houses, 
        hostels=hostels,
        businesses=businesses
    )
