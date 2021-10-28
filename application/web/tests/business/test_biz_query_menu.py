from app.business.biz_query_menu import BusinessPremisesQueryMenu

def test_city_query(client):
    with client.session_transaction() as session:
        city_query = BusinessPremisesQueryMenu(
            session=session,
            session_id="qwerty1234",
            user_response="1"
        )
        assert city_query.user_response == "1"
        assert city_query.search_business_premises_by_location()


def test_constituency_query(client):
    with client.session_transaction() as session:
        const_query = BusinessPremisesQueryMenu(
            session=session,
            session_id="qwerty1234",
            user_response="2"
        )
        assert const_query.user_response == "2"
        assert const_query.search_business_premises_by_location()

def test_ward_query(client):
    with client.session_transaction() as session:
        ward_query = BusinessPremisesQueryMenu(
            session=session,
            session_id="qwerty1234",
            user_response="3"
        )
        assert ward_query.user_response == "3"
        assert ward_query.search_business_premises_by_location()


def test_invalid_query_response(client):
    with client.session_transaction() as session:
        query = BusinessPremisesQueryMenu(
            session=session,
            session_id="qwerty123",
            user_response=""
        )
        assert query.user_response == ""
        assert query.search_business_premises_by_location()

def test_execute_menu(client):
    with client.session_transaction() as session:
        query = BusinessPremisesQueryMenu(
            session=session,
            session_id="qwerty123",
            user_response=""
        )
        query.session['level'] = 200
        assert query.session.get('level') is not None
        assert query.execute()