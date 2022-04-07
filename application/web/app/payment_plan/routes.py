from pydoc import render_doc
from flask import Blueprint, render_template, redirect, request, url_for, session
from app import db, models
from app.payment_plan.form import PaymentPlanForm

plan = Blueprint('plan', __name__)


@plan.route('/listing/property/<int:id>')
def listing_property(id):
    hostel = models.Hostels.query.filter_by(id=id).first()
    
    if hostel.units > 10:
        unit = hostel.units - 10 
        amount = round((0.10 * (unit * hostel.price)), 2) + 2000
    else:
        amount = 2000
    session['contacts'] = hostel.contacts
    session['amount'] = amount
    return render_template('listing/home.html', amount=amount, hostel=hostel)


@plan.route('/listing/home/<int:id>', methods=['POST', 'GET'])
def listing_home_page(id):
    hostel = models.Hostels.query.filter_by(id=id).first_or_404()
    plan_ = request.form.get('payment_plan')
    if 'weekly' in plan_:
        price = 0.10 * (hostel.units * hostel.price)
    elif 'monthly' in plan_:
        price = 0.07 * (hostel.units * hostel.price)
    else:
        price = 0.05 * (hostel.units * hostel.price)
    return render_template('listing/home.html', price=price)


@plan.route('/monthly/<int:id>', methods=['GET', 'POST'])
def monthly_plan(id):
    hostel = models.Hostels.query.filter_by(id=id).first_or_404()
    location = models.JsonFeature.query.filter_by(id=id).first_or_404()
    if request.method == 'POST':
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        units = request.form['units']
        price = request.form['price']
        plan = request.form['payment_plan']
        amount = request.form['amount']
        property_type = request.form['property_type']
        
        pplan = models.PaymentPlan(
            latitude=latitude,
            longitude=longitude,
            type_of_property=property_type,
            units=units,
            price=price,
            plan=plan,
            amount=amount
        )
        db.session.add(pplan)
        db.session.commit()
        return redirect(url_for('hostels.hostels_detail_view', id=hostel.id))
    return render_template('plan/month.html', hostel=hostel, location=location)


@plan.route('/plan/home/<int:id>', methods=['GET', 'POST'])
def plan_home(id):
    pplan = models.PaymentPlan.query.filter_by(id=id).first()
    return render_template('plan/home.html', pplan=pplan)