from mixer.backend.flask import mixer

from app import models 

def test_houses_models(client):
    houses = mixer.blend(models.Houses, type_of_house="Bedsitter")
    assert houses.type_of_house == "Bedsitter"

def test_hostels_models(client):
    hostels = mixer.blend(models.Hostels, school_name="Dedan Kimathi University Of Technology")
    assert hostels.school_name == "Dedan Kimathi University Of Technology"

def test_business_premises_models(client):
    business_premises = mixer.blend(models.BusinessPremises, type_of_business_premise="Offices")
    assert business_premises.type_of_business_premise == "Offices"

def test_lands_models(client):
    lands = mixer.blend(models.Land, county="Nairobi")
    assert lands.county == "Nairobi"