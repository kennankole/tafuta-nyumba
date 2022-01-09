
def test_home_page(client):
    response = client.post("/home")
    assert response.status_code == 200 
    assert b"Welcome to Tafuta-Nyumba" in response.data


def test_houses_page(client):
    response = client.post("/houses")
    assert response.status_code == 200
    assert b"Available Houses" in response.data
    

def test_hostels_page(client):
    response = client.post('/hostels')
    assert response.status_code == 200
    assert b"Available hostels" in response.data
    

def test_business_premises(client):
    response = client.post("/business")
    assert response.status_code == 200
    assert b"Available business premises" in response.data
    
    
    
    