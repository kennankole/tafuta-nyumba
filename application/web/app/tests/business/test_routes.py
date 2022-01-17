from app.models import BusinessPremises
from app import db

def test_business_list_view(client):
    response = client.get("/list")
    assert response.status_code == 200
    assert b"Available business premises" in response.data
    

def test_business_create_view_1(client):
    data = {
        "county": 'Nairobi',
        "constituency": 'Ruaraka',
        "ward": 'Korogocho',
        "name_of_city_or_town": "Kisumu",
        "street_name": "Tom Mboya",
        "type_of_business_premise": "Kibanda", 
        "area": 500,
        "units": 4,
        "price": 1500,
        "alternate_contact": +25474523356, 
        "for_rent":True
    }
    response = client.post("/create", data=data, follow_redirects=True)
    assert response.status_code == 200
    
    
def test_business_create_view_2(client):
    data = {
        "county": '#Nairobi',
        "constituency": '@Ruaraka',
        "ward": '12#Korogocho',
        "name_of_city_or_town": "12%Kisumu",
        "street_name": "Tom #$Mboya",
        "type_of_business_premise": "%^Kibanda", 
        "area": -500,
        "units": -4,
        "price": -1500,
        "alternate_contact": +25474523356, 
        "for_rent":True
    }
    response = client.post("/create", data=data, follow_redirects=True)
    assert response.status_code == 200
    
    
def test_biz_detail_view(client):
    response = client.get("/detail/1")
    assert response.status_code == 200
    
    
def test_biz_update_view_1(client):
    assert client.get('/update/1').status_code == 200
  
    data = {
        "units": -4,
        "price": -1500,
        "alternate_contact": +25474523356, 
        "for_rent":True
    }
    response = client.post('/update/1', data=data, follow_redirects=True)
    assert response.status_code == 200
    
    
def test_houses_update_view_2(client):
    assert client.get("/update/1").status_code == 200
    biz = BusinessPremises(county="Nakuru")
    db.session.add(biz)
    db.session.commit()
    data = {
        "units": 4,
        "price": 1500,
        "alternate_contact": +25474523356, 
        "for_rent":True
    }
    response = client.post("/update/{}".format(biz.id), data=data, follow_redirects=True)
    assert response.status_code == 200
    
    
def test_delete_business(client):
    assert client.get("/business/delete/6", data={}, follow_redirects=True).status_code == 200
    biz = BusinessPremises(county="Nairobi")
    db.session.add(biz)
    db.session.commit()
    response = client.get("/business/delete/{}".format(biz.id), follow_redirects=True)
    assert response.status_code == 404

    
    
    
    

    
    