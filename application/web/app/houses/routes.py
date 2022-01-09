from flask import (
    Blueprint, flash, 
    render_template, request, 
    url_for, redirect
)

from app import db
from app.models import Houses
from app.houses.forms import HouseRegistrationForm, UpdateHousesForm

bp = Blueprint('houses', __name__)


#House CreateView
@bp.route("/houses/data", methods=["GET", "POST"])
def create_houses():
    house = Houses()
    form = HouseRegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        form.populate_obj(house)
        db.session.add(house)
        db.session.commit()
        flash("Your property has been successfully registered")
        return redirect(url_for('views.home_page'))
    return render_template(
        'houses/create_houses.html',
        form=form
    )
    
#Houses Detailview
@bp.route("/house/data/<int:id>", methods=["GET"])
def houses_detail_view(id):
    house = Houses.query.get(id)
    try:
        return render_template('houses/house.html', house=house)
    except:
        return f"House does not exist"

# Houses ListViews
@bp.route('/houses', methods=["GET", "POST"])
def houses_list_view():
    houses = Houses.query.all()
    return render_template('houses/houses_list.html', houses=houses) 

# Houses UpdateView
@bp.route("/house/view/<int:id>", methods=["GET", "POST"])
def houses_update_view(id):
    house = Houses.query.get(id)
    form = UpdateHousesForm(obj=house)
    if form.validate_on_submit():
        form.populate_obj(house)
        db.session.commit()
        return redirect(url_for('houses.houses_detail_view', id=house.id))
    return render_template("houses/update_house.html", form=form)  


#Houses DeleteView
@bp.route("/delete/<int:id>", methods=("GET", "POST"))
def houses_delete_view(id):
    house = Houses.query.get(id)
    try:
        db.session.delete(house)
        db.session.commit()
        return redirect("/houses")
    except:
        return "The item could not be deleted"
