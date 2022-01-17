from flask import (
    Blueprint, url_for, 
    render_template, redirect
)
from flask.helpers import flash
from app import db
from app.models import BusinessPremises
from app.business.forms import BusinessPremisesRegistrationForm, BusinessPremisesUpdateForm

business = Blueprint("business", __name__)


@business.route("/list", methods=["GET"])
def business_list_view():
    biz = BusinessPremises.query.all()
    return render_template('business/list.html', biz=biz)


@business.route('/create', methods=['POST', 'GET'])
def business_create_view():
    biz = BusinessPremises()
    form = BusinessPremisesRegistrationForm()
    if form.validate_on_submit():
        form.populate_obj(biz)
        db.session.add(biz)
        db.session.commit()
        flash("Property successfully registered")
        return redirect(url_for('views.home_page'))
    return render_template('business/create.html', form=form)

@business.route('/detail/<int:id>', methods=['GET'])
def business_detail_view(id):
    try:
        biz = BusinessPremises.query.get(id)
        return render_template('/business/detail.html', biz=biz)
    except:
        return f"An Error occured!!"


@business.route('/update/<int:id>', methods=['POST', 'GET'])
def business_update_view(id):
    biz = BusinessPremises.query.get(id)
    form = BusinessPremisesUpdateForm(obj=biz)
    if form.validate_on_submit():
        form.populate_obj(biz)
        db.session.commit()
        flash("Your property has been successfully updated")
        return redirect(url_for('business.business_detail_view', id=biz.id))
    return render_template('business/update.html', form=form)



@business.route('/business/delete/<int:id>', methods=("GET", "POST"))
def business_delete_view(id):
    biz = BusinessPremises.query.get(id)
    try:
        db.session.delete(biz)
        db.session.commit()
        return redirect('business.business_list_view')
    except:
        return "Item could not be deleted"
        