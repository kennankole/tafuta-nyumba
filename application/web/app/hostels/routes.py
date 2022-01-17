from flask import (
    Blueprint, url_for, redirect, flash, render_template
)
from app.models import Hostels
from app import db
from app.hostels.forms import HostelRegistrationForm, HostelUpdateForm

hostels = Blueprint("hostels", __name__)



@hostels.route("/hostels", methods=["GET", "POST"])
def hostels_list_view():
    hostels = Hostels.query.all()
    return render_template('hostels/list.html', hostels=hostels)


@hostels.route("/hostels/create", methods=["POST", "GET"])
def hostels_create_view():
    form = HostelRegistrationForm()
    hostels = Hostels()
    if form.validate_on_submit():
        form.populate_obj(hostels)
        db.session.add(hostels)
        db.session.commit()
        flash("Your property has been successfully been registered")
        return redirect(url_for("views.home_page"))
    return render_template("hostels/create.html", form=form)
    

@hostels.route('/hostels/detail/<int:id>', methods=['GET', 'POST'])
def hostels_detail_view(id):
    try:
        hostel = Hostels.query.get(id)
        return render_template('hostels/detail.html', hostel=hostel)
    except:
        return "No property!!"
    
    
    
@hostels.route('/hostels/update/<int:id>', methods=['POST', 'GET'])
def hostels_update_view(id):
    hostels = Hostels.query.get(id)
    form = HostelUpdateForm(obj=hostels)
    if form.validate_on_submit():
        form.populate_obj(hostels)
        db.session.commit()
        return redirect(url_for('hostels.hostels_detail_view', id=hostels.id))
    return render_template('hostels/update.html', form=form)


@hostels.route('/hostels/delete/<int:id>', methods=['GET', 'POST'])
def hostels_delete_view(id):
    hostels = Hostels.query.get(id)
    try:
        db.session.delete(hostels)
        db.session.commit()
        return redirect('/houses')
    except:
        return "This item could not be deleted"