from app.houses.houses_query_menu import HousesQueryMenu

counties = [
    "Nairobi", "Kisumu"
]
constituncies = [
    "Ruaraka"
]
ward = [
    "Korogocho"
]

regex = "[0-9]~!@#$%^&*()_-+={[}]|\?/><.,"

def test_constituency_query(client):
    with client.session_transaction() as session:
        county_query = HousesQueryMenu(
            session=session,
            session_id="qwerty123",
            user_response="1"
        )
        assert county_query.user_response == "1"
        assert county_query.search_houses_by_location()

def test_ward_query(client):
    with client.session_transaction() as session:
        county_query = HousesQueryMenu(
            session=session,
            session_id="qwerty123",
            user_response="2"
        )
        assert county_query.user_response == "2"
        assert county_query.search_houses_by_location()

def test_estate_village_query(client):
    with client.session_transaction() as session:
        county_query = HousesQueryMenu(
            session=session,
            session_id="qwerty123",
            user_response="3"
        )
        assert county_query.user_response == "3"
        assert county_query.search_houses_by_location()

def test_invalid_query_response(client):
    with client.session_transaction() as session:
        county_query = HousesQueryMenu(
            session=session,
            session_id="qwerty123",
            user_response=""
        )
        assert county_query.user_response == ""
        assert county_query.search_houses_by_location()


def test_execute_menu(client):
    with client.session_transaction() as session:
        county_query = HousesQueryMenu(
            session=session,
            session_id="qwerty123",
            user_response=""
        )
        county_query.session['level'] = 50
        assert county_query.session.get('level') is not None
        assert county_query.execute()