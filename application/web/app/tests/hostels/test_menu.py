from app.hostels.menu import HostelsQueryMenu
from app.hostels.registration import HostelsRegistrationMenu


def test_search_hostels_by_school_name(client):
    with client.session_transaction() as session:
        hostels_query_menu = HostelsQueryMenu(
            session=session, session_id="qwerty124", user_response="1"
        )
        assert hostels_query_menu.user_response == "1"
        assert hostels_query_menu.hostels_searching_menu()

def test_search_hostels_by_constituency(client):
    with client.session_transaction() as session:
        hostels_query_menu = HostelsQueryMenu(
            session=session, session_id="qwerty124", user_response="2"
        )
        assert hostels_query_menu.user_response == "2"
        assert hostels_query_menu.hostels_searching_menu()


def test_search_hostels_by_ward(client):
    with client.session_transaction() as session:
        hostels_query_menu = HostelsQueryMenu(
            session=session, session_id="qwerty124", user_response="3"
        )
        assert hostels_query_menu.user_response == "3"
        assert hostels_query_menu.hostels_searching_menu()


def test_invalid_input_hostels_search(client):
    with client.session_transaction() as session:
        hostels_query_menu = HostelsQueryMenu(
            session=session, session_id="qwerty124", user_response="#$"
        )
        assert hostels_query_menu.user_response == "#$"
        assert hostels_query_menu.hostels_searching_menu()


def test_register_hostels(client):
    with client.session_transaction() as session:
        hostels_query_menu = HostelsRegistrationMenu(
            session=session, session_id="qwerty124", user_response="1"
        )
        assert hostels_query_menu.user_response == "1"
        assert hostels_query_menu.hostels_registration_menu()


def test_decline_hostel_registeration(client):
    with client.session_transaction() as session:
        hostels_query_menu = HostelsRegistrationMenu(
            session=session, session_id="qwerty124", user_response="2"
        )
        assert hostels_query_menu.user_response == "2"
        assert hostels_query_menu.hostels_registration_menu()


def test_hostels_execute_menu(client):
    with client.session_transaction() as session:
        execute_menu = HostelsQueryMenu(
            session_id="qwerty124", session=session, user_response="1"
        )
        assert execute_menu.execute()
