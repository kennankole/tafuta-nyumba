import os
from statistics import mode
from flask import Blueprint, flash, redirect, render_template, request, url_for, jsonify
from app import models, db



map = Blueprint('map', __name__)

basedir = os.path.abspath(os.path.dirname(__file__))

@map.route('/map', methods=['GET', 'POST'])
def home():
    gis_coord = models.JsonFeature().get_all_coordinates_to_geojson()
    return render_template('maps/home.html', gis_coord=gis_coord)
    

@map.route('/save/location', methods=['GET', 'POST'])
def capture_location_data():
    lat = request.form['latitude']
    lon = request.form['longitude']
    county = request.form['county']
    return f"{lat, lon, county}"
    # flash("You property has been added successfully!!")
    # return redirect(url_for('map.property_view', id=json_feature.id))


@map.route('/property/<int:id>/', methods=['GET'])
def property_view(id):
    hstl_lctn = models.Hostels().get_hostel_coordinate_to_geojson(id=id)
    # hstl_all_lctn = models.Hostels().get_all__hostel_coordinates_to_geojson()
    hostel = models.Hostels.query.filter_by(id=id).first()
    # photo = models.HostelsGallery.query.filter_by(id=id).first_or_404()
    # feature = models.JsonFeature.query.filter_by(id=id).first_or_404()
    # property_coord = models.JsonFeature().get_property_location(id=id)
    # gis_coord= models.JsonFeature().get_all_coordinates_to_geojson()
    # print(property_coord['geometry']['coordinates'])
    return render_template('maps/index.html', hstl_lctn=hstl_lctn, hostel=hostel)


