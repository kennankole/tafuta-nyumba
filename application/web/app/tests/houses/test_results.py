from sqlalchemy.sql.functions import mode
from app.houses.results import HousesQueryResults
from app import models
from mixer.backend.flask import mixer

def test_rental_houses_by_constituency(client):
    with client.session_transaction() as session:
        const_menu = HousesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        const_menu.session["rent_house"] = "1"
        rent = True
        assert rent
        assert const_menu.session.get("rent_house")
        assert const_menu.houses_const_query_results()
        assert const_menu.houses_ward_query_results()
        assert const_menu.houses_village_estate_query_results()


def test_houses_for_sale_by_constituency(client):
    with client.session_transaction() as session:
        const_menu = HousesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        const_menu.session["buy_house"] = "4"
        rent = False
        assert not rent
        assert const_menu.session.get("buy_house")
        assert const_menu.houses_const_query_results()
        assert const_menu.houses_ward_query_results()
        assert const_menu.houses_village_estate_query_results()


def test_houses_query_results_execute(client):
    with client.session_transaction() as session:
        exec_menu = HousesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        assert exec_menu.execute()



def test_houses_const_2_results(client):
    with client.session_transaction() as session:
        const_menu = HousesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.cycle(6).blend(models.Houses, type_of_house="Bedsitter", for_rent=True, constituency="Ruaraka")
        assert models.Houses.query.filter_by(constituency="Ruaraka", for_rent=True, type_of_house="Bedsitter").count() > 2
        assert models.Houses.get_const_houses(const="Ruaraka", hse_type="Bedsitter", rent=True)
        assert const_menu.houses_const_query_results()
        
def test_houses_const_1_results(client):
    with client.session_transaction() as session:
        const_menu = HousesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.blend(models.Houses, type_of_house="Bedsitter", for_rent=True, constituency="Ruaraka")
        assert models.Houses.get_const_houses(const="Ruaraka", hse_type="Bedsitter", rent=True)
        assert const_menu.houses_const_query_results()
        
        
def test_houses_ward_2_results(client):
    with client.session_transaction() as session:
        const_menu = HousesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.cycle(3).blend(models.Houses, type_of_house="Bedsitter", for_rent=True, constituency="Ruaraka", ward="Korogocho")
        assert models.Houses.query.filter_by(constituency="Ruaraka", for_rent=True,type_of_house="Bedsitter").count() > 2
        assert models.Houses.get_ward_houses(ward="Korogocho", hse_type="Bedsitter", rent=True)
        assert const_menu.houses_ward_query_results()
        
def test_houses_ward_1_results(client):
    with client.session_transaction() as session:
        const_menu = HousesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.blend(models.Houses, type_of_house="Bedsitter", for_rent=True, constituency="Ruaraka", ward="Korogocho")
        assert models.Houses.get_ward_houses(ward="Korogocho", hse_type="Bedsitter", rent=True)
        assert const_menu.houses_ward_query_results()
        
def test_houses_ward_0_results(client):
    with client.session_transaction() as session:
        const_menu = HousesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.blend(models.Houses)
        assert models.Houses.get_ward_houses(ward="Korogocho", hse_type="Bedsitter", rent=True)
        assert const_menu.houses_ward_query_results()
        
        
def test_houses_ward_2_results(client):
    with client.session_transaction() as session:
        const_menu = HousesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.cycle(3).blend(models.Houses, type_of_house="Bedsitter", for_rent=True, constituency="Ruaraka", ward="Korogocho")
        assert models.Houses.query.filter_by(constituency="Ruaraka", for_rent=True,type_of_house="Bedsitter").count() > 2
        assert models.Houses.get_ward_houses(ward="Korogocho", hse_type="Bedsitter", rent=True)
        assert const_menu.houses_ward_query_results()
        
        
        
def test_houses_village_1_results(client):
    with client.session_transaction() as session:
        const_menu = HousesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.blend(models.Houses, type_of_house="Bedsitter", for_rent=True, constituency="Ruaraka", name_of_estate_or_village="Ngomongo")
        assert models.Houses.get_village_houses(name="Ngomongo", hse_type="Bedsitter", rent=True)
        assert const_menu.houses_village_estate_query_results()
 
def test_houses_village_2_results(client):
    with client.session_transaction() as session:
        const_menu = HousesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.cycle(3).blend(models.Houses, type_of_house="Bedsitter", for_rent=True, constituency="Ruaraka", name_of_estate_or_village="Ngomongo")
        assert models.Houses.query.filter_by(constituency="Ruaraka", for_rent=True, type_of_house="Bedsitter").count() > 2
        assert models.Houses.get_village_houses(name="Ngomongo", hse_type="Bedsitter", rent=True)
        assert const_menu.houses_ward_query_results()
        
                
def test_houses_village_0_results(client):
    with client.session_transaction() as session:
        const_menu = HousesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.blend(models.Houses)
        assert models.Houses.get_village_houses(name="Ngomongo", hse_type="Bedsitter", rent=True)
        assert const_menu.houses_village_estate_query_results()
        