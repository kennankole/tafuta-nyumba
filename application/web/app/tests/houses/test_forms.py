
 
def test_invalid_fields(client):
    data = {
        "county": '#$%$@345irobi',
        "constituency": '#$%$@345araka',
        "ward": '#$%$@345rogocho',
        "name_of_estate_or_village":'#$%$@345Highridge',
        "units": -4,
        "price": -1500,
        "type_of_house": '#$%$@345Single room',
        "alternate_contact": +25474523356, 
        "for_rent":True
    }
    response = client.post("/houses/data", data=data, follow_redirects=True)
    assert response.status_code == 200
    

 
    