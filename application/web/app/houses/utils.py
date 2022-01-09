from app.models import Houses


def get_type_of_house(id, type_of_houses):
    return type_of_houses.get(id)

def results_const_helper_func(const, renting, hse_type):
    
    if Houses.query.filter_by(constituency=const, for_rent=renting, type_of_house=hse_type).count() > 2:
        return True
    else:
        return False
    
def results_ward_helper_func(ward, renting, hse_type):
    if Houses.query.filter_by(ward=ward, for_rent=renting, type_of_house=hse_type).count() > 2:
        return True
    else:
        return False
    

def results_village_helper_func(name, renting, hse_type):
    if Houses.query.filter_by(name_of_estate_or_village=name, for_rent=renting, type_of_house=hse_type).count() > 2:
        return True
    else:
        return False
