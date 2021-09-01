from app.models import Houses
from app.houses.results import HousesQueryResults
from mixer.backend.flask import mixer

def test_rental_houses_by_constituency(client):
    with client.session_transaction() as session:
        const_menu = HousesQueryResults(
            session=session,
            session_id="qwerty123",
            user_response="Ruaraka"
        )
        const_menu.session['rent_house'] = "1"
        rent = True
        assert rent
        assert const_menu.session.get('rent_house')
        assert const_menu.houses_const_query_results()
        assert const_menu.houses_ward_query_results()
        assert const_menu.houses_village_estate_query_results()

def test_houses_for_sale_by_constituency(client):
    with client.session_transaction() as session:
        const_menu = HousesQueryResults(
            session=session,
            session_id="qwerty123",
            user_response="Ruaraka"
        )
        const_menu.session['buy_house'] = "4"
        rent = False
        assert not rent
        assert const_menu.session.get('buy_house')
        assert const_menu.houses_const_query_results()
        assert const_menu.houses_ward_query_results()
        assert const_menu.houses_village_estate_query_results()






