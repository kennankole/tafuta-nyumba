from app.hostels.hostels_base_menu import HostelsMainMenu


def test_hostels_main_menu_rent(client):
    with client.session_transaction() as session:
        hostels_menu = HostelsMainMenu(
            session=session, session_id="1340rewq054", user_response="1"
        )
        assert hostels_menu.hostels_services_menu()


def test_hostels_main_menu_rent_out(client):
    with client.session_transaction() as session:
        hostels_menu = HostelsMainMenu(
            session=session, session_id="1340rewq054", user_response="2"
        )
        assert hostels_menu.hostels_services_menu()


def test_hostels_main_menu_invalid_entry(client):
    with client.session_transaction() as session:
        hostels_menu = HostelsMainMenu(
            session=session, session_id="1340rewq054", user_response=""
        )
        assert hostels_menu.hostels_services_menu()


def test_hostels_main_menu(client):
    with client.session_transaction() as session:
        hostels_menu = HostelsMainMenu(
            session=session, session_id="1340rewq054", user_response="1"
        )
        assert hostels_menu.execute()
