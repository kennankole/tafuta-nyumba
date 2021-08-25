from app.houses.houses_base_menu import HousesMainMenu

def test_houses_main_menu_rent(client):
    with client.session_transaction() as session:
        houses_menu = HousesMainMenu(
            session=session,
            session_id="1340rewq054",
            user_response="1"
        )
        assert houses_menu.house_services_menu()


def test_houses_main_menu_rent_out(client):
    with client.session_transaction() as session:
        houses_menu = HousesMainMenu(
            session=session,
            session_id="1340rewq054",
            user_response="2"
        )
        assert houses_menu.house_services_menu()


def test_houses_main_menu_buy(client):
    with client.session_transaction() as session:
        houses_menu = HousesMainMenu(
            session=session,
            session_id="1340rewq054",
            user_response="3"
        )
        assert houses_menu.house_services_menu()


def test_houses_main_menu_selling(client):
    with client.session_transaction() as session:
        houses_menu = HousesMainMenu(
            session=session,
            session_id="1340rewq054",
            user_response="4"
        )
        assert houses_menu.house_services_menu()


def test_houses_main_menu_invalid_entry(client):
    with client.session_transaction() as session:
        houses_menu = HousesMainMenu(
            session=session,
            session_id="1340rewq054",
            user_response=""
        )
        assert houses_menu.house_services_menu()


def test_houses_main_menu(client):
    with client.session_transaction() as session:
        houses_menu = HousesMainMenu(
            session=session,
            session_id="1340rewq054",
            user_response="1"
        )
        assert houses_menu.execute()


