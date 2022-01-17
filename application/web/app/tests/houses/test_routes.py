from app.models import Houses
from app.houses.forms import UpdateHousesForm
from app import db
import json

def test_houses_list_view(client):
    response = client.get("/houses")
    assert response.status_code == 200
    assert b"Available Houses" in response.data
    
    
def test_creating_house(client):
    data = {
        "county": 'Nairobi',
        "constituency": 'Ruaraka',
        "ward": 'Korogocho',
        "name_of_estate_or_village": 'Highridge',
        "type_of_house": 'Single room',
        "units": 4,
        "price": 1500,
        "alternate_contact": +25474523356, 
        "for_rent":True
    }
    response = client.post("/houses/data", data=data, follow_redirects=True)
    assert response.status_code == 200



def test_house_detail_view_1(client):
    response = client.get("/house/data/1")
    assert response.status_code == 200
    assert b"House does not exist" in response.data 


def test_houses_update_view_1(client):
    data = {
        "units": -4,
        "price": -1500,
        "alternate_contact": +25474523356, 
        "for_rent":True
    }
    assert client.get("/house/view/1").status_code == 200
    response = client.post("/house/view/1", data=data, follow_redirects=True)
    assert response.status_code == 200
    
    
def test_houses_update_view_2(client):
    assert client.get("/house/view/1").status_code == 200
    house = Houses(county="Nakuru")
    db.session.add(house)
    db.session.commit()
    data = {
        "units": 4,
        "price": 1500,
        "alternate_contact": +25474523356, 
        "for_rent":True
    }
    response = client.post("/house/view/{}".format(house.id), data=data, follow_redirects=True)
    assert response.status_code == 200
    
def test_delete_house_property_2(client):
    assert client.post("/delete/6", data={}, follow_redirects=True).status_code == 200
    house = Houses(county="Nairobi")
    db.session.add(house)
    db.session.commit()
    response = client.get("/delete/{}".format(house.id), follow_redirects=True)
    assert response.status_code == 200
    
    

    
    


