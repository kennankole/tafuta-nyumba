from flask import request

def test_home_page(client):
    home = client.get('/')
    assert request.path == "/"
    assert b'Welcome to Tafuta Nyumba' in home.data