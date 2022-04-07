import os
from PIL import Image
import secrets 
from flask_login import login_required, current_user
from flask import (
    Blueprint, request, session, url_for, redirect, flash, render_template
)
from werkzeug.utils import secure_filename
from app.models import Hostels, User
from app import db, create_app
from app.hostels.forms import HostelUpdateForm
from app import models


hostels = Blueprint("hostels", __name__)

app = create_app()

# Save photo helper function
def save_photo(picture):
    try:
        random_no = secrets.token_hex(8)
        _, f_ext = os.path.splitext(picture.filename)
        picture_name = random_no + f_ext
        picture_path = os.path.join(app.root_path, 'static/photos', picture_name)
        
        output_size = (250, 250)
        i = Image.open(picture)
        i.thumbnail(output_size)
        i.save(picture_path)
        return picture_name
    except:
        pass
    return

# Hostel assets lists view
@hostels.route('/hostels/home')
@login_required
def hostels_home():
    user = models.User.query.filter_by(id=current_user.id).first()
    return render_template('hostels/home_page.html', user=user)


# Hostel Create view
@hostels.route('/create/hostels', methods=['GET', 'POST'])
@login_required
def create_hostels():
    user = User.query.filter_by(id=current_user.id).first_or_404()
    if request.method == 'POST':
        
        hostel = Hostels(
            county=request.form['county'],
            constituency=request.form['constituency'],
            ward=request.form['ward'],
            school_name=request.form['school_name'],
            units=request.form['units'],
            price=request.form['price'],
            listing_status=request.form.get('listing'),
            contacts=request.form['contacts_1'],
            alternate_contact=request.form['contacts_2'],
            latitude=request.form['latitude'],
            longitude=request.form['longitude']
        )
        db.session.add(hostel)
        db.session.commit()
        user.hostel_asset.append(hostel)
        db.session.commit()
        return redirect(url_for('hostels.hostels_home'))
    return render_template('maps/home.html')

def amount(units, price):
    pass
    

# Hostel detail view
@hostels.route('/detail/<int:id>', methods=['GET', 'POST']) 
@login_required
def hostels_detail_view(id):
    hostel = Hostels.query.get(id)
    return render_template('hostels/detail.html', hostel=hostel)

  

# Hostel Update view
@hostels.route('/hostels/update/<int:id>', methods=['POST', 'GET'])
@login_required 
def hostels_update_view(id):
    hostels = Hostels.query.get(id)
    form = HostelUpdateForm()
    if form.validate_on_submit():
        if form.photo.data:
            photo_file = save_photo(form.photo.data)
            hostels.photo = photo_file
        hostels.price = form.price.data
        hostels.units = form.units.data 
        hostels.alternate_contact = form.alternate_contact.data
        db.session.commit()
        flash("Your hostel property has been updated successfully")
        return redirect(url_for('hostels.hostels_detail_view', id=hostels.id))
    elif request.method == 'GET':
        form.price.data = hostels.price
        form.units.data = hostels.units
        form.contacts.data = hostels.contacts
        form.alternate_contact.data = hostels.alternate_contact
    return render_template('hostels/update.html', form=form, hostels=hostels)


# Hostel Delete view
@hostels.route('/hostels/delete/<int:id>', methods=['GET', 'POST'])
@login_required 
def hostels_delete_view(id):
    hostels = Hostels.query.get(id)
    try:
        db.session.delete(hostels)
        db.session.commit()
        return redirect('/houses')
    except:
        return "This item could not be deleted"

