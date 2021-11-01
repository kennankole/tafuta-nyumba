from mixer.backend.flask import mixer
import pytest
from app.models import Houses
from app import models


def test_houses_models(client):
    with client.session_transaction() as session:
        houses = mixer.blend(models.Houses, type_of_house="Bedsitter")
        assert houses.type_of_house == "Bedsitter"


def test_hostels_models(client):
    with client.session_transaction() as session:
        hostels = mixer.blend(
            models.Hostels, school_name="Dedan Kimathi University Of Technology"
        )
        assert hostels.school_name == "Dedan Kimathi University Of Technology"


def test_business_premises_models(client):
    with client.session_transaction() as session:
        business_premises = mixer.blend(
            models.BusinessPremises, type_of_business_premise="Offices"
        )
        assert business_premises.type_of_business_premise == "Offices"


def test_lands_models(client):
    with client.session_transaction() as session:
        lands = mixer.blend(models.Land, county="Nairobi")
        assert lands.county == "Nairobi"
