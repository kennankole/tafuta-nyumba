from app.houses.menu import HousesQueryMainMenu


def test_search_rental_houses(client):
    with client.session_transaction() as session:

        rent_query_menu = HousesQueryMainMenu(
            session=session, session_id="134083wrouow4", user_response="1"
        )
        assert rent_query_menu.user_response in ("1", "2", "3", "4", "5", "6")
        assert rent_query_menu.search_houses_to_rent_by_location()
        assert rent_query_menu.execute()


def test_rental_house_registration(client):
    with client.session_transaction() as session:
        rental_house_registration_menu = HousesQueryMainMenu(
            session=session,
            session_id="qeqer0809r",
            user_response="11",
        )
        assert rental_house_registration_menu.user_response in (
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
        )
        assert rental_house_registration_menu.rental_houses_registration()


def test_search_houses_for_sale(client):
    with client.session_transaction() as session:
        houses_for_sale_menu = HousesQueryMainMenu(
            session_id="qerq4234qdfaf", session=session, user_response="10"
        )
        assert houses_for_sale_menu.user_response in ("10", "20", "30", "40")
        assert houses_for_sale_menu.search_houses_to_buy_by_location()


def test_register_houses_for_sale(client):
    with client.session_transaction() as session:
        houses_for_sale_registraion_menu = HousesQueryMainMenu(
            session_id="qerq4234qdfaf", session=session, user_response="50"
        )

        assert houses_for_sale_registraion_menu.user_response in (
            "50",
            "60",
            "70",
            "80",
        )
        assert houses_for_sale_registraion_menu.register_houses_for_sale()
