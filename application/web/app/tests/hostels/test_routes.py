from app.models import Hostels
from app import db


def test_hostels_list_view(client):
    response = client.get("/hostels")
    assert response.status_code == 200
    assert b"Available Hostels" in response.data
    
    
def test_valid_fields(client):
    data = {
        "county": 'Nairobi',
        "constituency": 'Ruaraka',
        "ward": 'Korogocho',
        "name_of_estate_or_village":'Highridge',
        "school_name": 'Dedan Kimathi University',
        "units": 4,
        "price": 1500,
        "alternate_contact": +25474523356, 
        "for_rent":True
    }
    response = client.post("/hostels/create", data=data, follow_redirects=True)
    assert response.status_code == 200


def test_invalid_fields(client):
    data = {
        "county": '#$%$@345irobi',
        "constituency": '#$%$@345araka',
        "ward": '#$%$@345rogocho',
        "school_name": '#Dedan Kimathi University',
        "units": -4,
        "price": -1500,
        "alternate_contact": +25474523356, 
        "for_rent":True
    }
    response = client.post("/hostels/create", data=data, follow_redirects=True)
    assert response.status_code == 200
    
    
def test_hostels_detail_view_1(client):
    response = client.get("/hostels/detail/1")
    assert response.status_code == 200
    
  
 
    


def test_houses_update_view_1(client):
    data = {
        "units": -4,
        "price": -1500,
        "alternate_contact": +25474523356, 
        "for_rent":True
    }
    assert client.get("/hostels/update/1").status_code == 200
    response = client.post("/hostels/update/1", data=data, follow_redirects=True)
    assert response.status_code == 200
    
    
def test_houses_update_view_2(client):
    assert client.get("/hostels/update/1").status_code == 200
    house = Hostels(county="Nakuru")
    db.session.add(house)
    db.session.commit()
    data = {
        "units": 4,
        "price": 1500,
        "alternate_contact": +25474523356, 
        "for_rent":True
    }
    response = client.post("/hostels/update/1", data=data, follow_redirects=True)
    assert response.status_code == 200
    
def test_delete_house_property_2(client):
    assert client.post("hostels/delete/6", data={}, follow_redirects=True).status_code == 200
    house = Hostels(county="Nairobi")
    db.session.add(house)
    db.session.commit()
    response = client.get("hostels/delete/{}".format(house.id), follow_redirects=True)
    assert response.status_code == 200
    
    

    
    


