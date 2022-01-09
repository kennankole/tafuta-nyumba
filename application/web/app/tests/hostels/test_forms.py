from app.hostels.forms import HostelRegistrationForm

def test_hostel_registration_form(client):
    data = {
        "county": 'Nairobi',
        "constituency": 'Ruaraka',
        "ward": 'Korogocho',
        "name_of_estate_or_village":'Highridge',
        "type_of_house": 'Single room',
        "units": 4,
        "price": 1500,
        "alternate_contact": +25474523356, 
        "for_rent":True
    }
    response = client.post("/hostels/data", data=data, follow_redirects=True)
    assert response.status_code == 200