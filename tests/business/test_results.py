from app.business.results import BusinessPremisesQueryResults


def test_rental_business_premises(client):
    with client.session_transaction() as session:
        const_menu = BusinessPremisesQueryResults(
            session=session,
            session_id="qwerty123",
            user_response="Ruaraka"
        )
        const_menu.session['rent_business'] = "1"
        rent = True
        assert rent
        assert const_menu.session.get('rent_business')
        assert const_menu.biz_premises_const_query_results()
        assert const_menu.biz_premises_city_or_town_results()
        assert const_menu.biz_premises_ward_query_results()

def test_business_premises_for_sale(client):
    with client.session_transaction() as session:
        const_menu = BusinessPremisesQueryResults(
            session=session,
            session_id="qwerty123",
            user_response="Ruaraka"
        )
        const_menu.session['buy_business'] = "3"
        rent = False
        assert not rent
        assert const_menu.session.get('buy_business')
        assert const_menu.biz_premises_const_query_results()
        assert const_menu.biz_premises_city_or_town_results()
        assert const_menu.biz_premises_ward_query_results()
        

def test_business_premises_query_results_execute(client):
    with client.session_transaction() as session:
        exec_menu = BusinessPremisesQueryResults(
            session=session,
            session_id="qwerty123",
            user_response="Ruaraka"
        )
        assert exec_menu.execute()