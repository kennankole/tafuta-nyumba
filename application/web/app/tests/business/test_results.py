from app.business.results import BusinessPremisesQueryResults
from app.models import BusinessPremises
from mixer.backend.flask import mixer


def test_rental_business_premises(client):
    with client.session_transaction() as session:
        const_menu = BusinessPremisesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        const_menu.session["rent_business"] = "1"
        rent = True
        assert rent
        assert const_menu.session.get("rent_business")
        assert const_menu.biz_premises_const_query_results()
        assert const_menu.biz_premises_city_or_town_results()
        assert const_menu.biz_premises_ward_query_results()


def test_business_premises_for_sale(client):
    with client.session_transaction() as session:
        const_menu = BusinessPremisesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        const_menu.session["buy_business"] = "3"
        rent = False
        assert not rent
        assert const_menu.session.get("buy_business")
        assert const_menu.biz_premises_const_query_results()
        assert const_menu.biz_premises_city_or_town_results()
        assert const_menu.biz_premises_ward_query_results()


def test_business_premises_query_results_execute(client):
    with client.session_transaction() as session:
        exec_menu = BusinessPremisesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        assert exec_menu.execute()
        

def test_business_const_1_results(client):
    with client.session_transaction() as session:
        const_menu = BusinessPremisesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.blend(BusinessPremises, type_of_business_premise="Kibanda", for_rent=True, constituency="Ruaraka")
        assert BusinessPremises.get_const_business(const="Ruaraka", hse_type="Kibanda", rent=True)
        assert const_menu.biz_premises_const_query_results()
        
def test_business_const_2_results(client):
    with client.session_transaction() as session:
        const_menu = BusinessPremisesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.cycle(3).blend(BusinessPremises, type_of_business_premise="Kibanda", for_rent=True, constituency="Ruaraka")
        assert BusinessPremises.get_const_business(const="Ruaraka", hse_type="Kibanda", rent=True)
        assert const_menu.biz_premises_const_query_results()
        
def test_business_const_0_results(client):
    with client.session_transaction() as session:
        const_menu = BusinessPremisesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.blend(BusinessPremises)
        assert BusinessPremises.get_const_business(const="Ruaraka", hse_type="Kibanda", rent=True)
        assert const_menu.biz_premises_const_query_results()
        
        
def test_business_ward_2_results(client):
    with client.session_transaction() as session:
        const_menu = BusinessPremisesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.cycle(3).blend(BusinessPremises, type_of_business_premise="Kibanda", for_rent=True, constituency="Ruaraka", ward="Korogocho")
        assert BusinessPremises.query.filter_by(constituency="Ruaraka", for_rent=True, type_of_business_premise="Kibanda").count() > 2
        assert BusinessPremises.get_ward_business(ward="Korogocho", hse_type="Kibanda", rent=True)
        assert const_menu.biz_premises_ward_query_results()
        
def test_business_ward_1_results(client):
    with client.session_transaction() as session:
        const_menu = BusinessPremisesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.blend(BusinessPremises, type_of_business_premise="Kibanda", for_rent=True, constituency="Ruaraka", ward="Korogocho")
        assert BusinessPremises.get_ward_business(ward="Korogocho", hse_type="Kibanda", rent=True)
        assert const_menu.biz_premises_ward_query_results()
        
def test_business_ward_0_results(client):
    with client.session_transaction() as session:
        const_menu = BusinessPremisesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.blend(BusinessPremises)
        assert BusinessPremises.get_ward_business(ward="Korogocho", hse_type="Kibanda", rent=True)
        assert const_menu.biz_premises_ward_query_results()
           
        
def test_business_village_or_city_1_results(client):
    with client.session_transaction() as session:
        const_menu = BusinessPremisesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        
        mixer.blend(BusinessPremises, type_of_business_premise="Kibanda", for_rent=True, constituency="Ruaraka", name_of_city_or_town="Ngomongo")
        # assert BusinessPremises.query.filter_by(name_of_city_or_town="Ngomongo").count() < 2
        assert BusinessPremises.get_name_of_city_business(name="Ngomongo", hse_type="Kibanda", rent=True)
        assert const_menu.biz_premises_city_or_town_results()
        
 
def test_business_village_or_city_2_results(client):
    with client.session_transaction() as session:
        const_menu = BusinessPremisesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.cycle(3).blend(BusinessPremises, type_of_business_premise="Kibanda", for_rent=True, constituency="Ruaraka", name_of_city_or_town="Ngomongo")
        assert BusinessPremises.query.filter_by(constituency="Ruaraka", for_rent=True, type_of_business_premise="Kibanda").count() > 2
        assert BusinessPremises.get_name_of_city_business(name="Ngomongo", hse_type="Kibanda", rent=True)
        assert const_menu.biz_premises_city_or_town_results()
        
                
def test_business_village_or_city_0_results(client):
    with client.session_transaction() as session:
        const_menu = BusinessPremisesQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.blend(BusinessPremises)
        assert BusinessPremises.get_name_of_city_business(name="Ngomongo", hse_type="Kibanda", rent=True)
        assert const_menu.biz_premises_city_or_town_results()
        