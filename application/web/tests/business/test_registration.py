import re
from app.business.registration import BusinessPremisesRegistrationMenu


def test_biz_premises_registration_consent_agree(client):
    with client.session_transaction() as session:
        reg_menu = BusinessPremisesRegistrationMenu(
            session=session, session_id="qwerty12345", user_response="1"
        )
        reg_menu.session["level"] = 30
        assert reg_menu.session.get("level") == 30
        assert reg_menu.user_response == "1"
        assert reg_menu.execute()


def test_biz_premises_registration_consent_decline(client):
    with client.session_transaction() as session:
        reg_menu = BusinessPremisesRegistrationMenu(
            session=session, session_id="qwerty12345", user_response="2"
        )
        reg_menu.session["level"] = 30
        assert reg_menu.session.get("level") == 30
        assert reg_menu.execute()


def test_biz_premises_rental_registration_consent_invalid_input(client):
    with client.session_transaction() as session:
        reg_menu = BusinessPremisesRegistrationMenu(
            session=session, session_id="qwerty12345", user_response=""
        )
        reg_menu.session["level"] = 30
        reg_menu.session["rent_out_biz_premises"] = "2"
        assert reg_menu.user_response not in ("1", "2")
        assert reg_menu.session.get("level") == 30
        assert reg_menu.session.get("rent_out_biz_premises") == "2"
        assert reg_menu.execute()


def test_biz_premises_for_sale_registration_consent_invalid_input(client):
    with client.session_transaction() as session:
        reg_menu = BusinessPremisesRegistrationMenu(
            session=session, session_id="qwerty12345", user_response=""
        )
        reg_menu.session["level"] = 30
        reg_menu.session["sell_business"] = "4"
        assert reg_menu.session.get("level") == 30
        assert reg_menu.user_response not in ("1", "2")
        assert reg_menu.session.get("sell_business") == "4"
        assert reg_menu.execute()


def test_get_county(client):
    with client.session_transaction() as session:
        county_menu = BusinessPremisesRegistrationMenu(
            session=session, session_id="qwerty12345", user_response=""
        )
        county_menu.session["level"] = 31
        assert county_menu.session.get("level") == 31
        assert county_menu.execute()


def test_get_constituency(client):
    with client.session_transaction() as session:
        const_menu = BusinessPremisesRegistrationMenu(
            session=session, session_id="qwerty12345", user_response=""
        )
        const_menu.session["level"] = 32
        assert const_menu.session.get("level") == 32
        assert const_menu.execute()


def test_get_ward(client):
    with client.session_transaction() as session:
        ward_menu = BusinessPremisesRegistrationMenu(
            session=session, session_id="qwerty12345", user_response=""
        )
        ward_menu.session["level"] = 33
        assert ward_menu.session.get("level") == 33
        assert ward_menu.execute()


def test_town_or_city_name(client):
    with client.session_transaction() as session:
        town_city_menu = BusinessPremisesRegistrationMenu(
            session=session, session_id="qwerty12345", user_response=""
        )
        town_city_menu.session["level"] = 34
        assert town_city_menu.session.get("level") == 34
        assert town_city_menu.execute()


def test_get_street(client):
    with client.session_transaction() as session:
        street_name = BusinessPremisesRegistrationMenu(
            session=session, session_id="qwerty12345", user_response=""
        )
        street_name.session["level"] = 35
        assert street_name.session.get("level") == 35
        assert street_name.execute()


def test_get_units(client):
    with client.session_transaction() as session:
        units_menu = BusinessPremisesRegistrationMenu(
            session=session, session_id="qwerty12345", user_response="3"
        )
        units_menu.session["level"] = 36
        assert units_menu.session.get("level") == 36
        assert units_menu.user_response == "3"
        assert units_menu.execute()


def test_get_premises_floor_area(client):
    with client.session_transaction() as session:
        units_menu = BusinessPremisesRegistrationMenu(
            session=session, session_id="qwerty12345", user_response="750"
        )
        units_menu.session["level"] = 37
        assert units_menu.session.get("level") == 37
        assert units_menu.user_response == "750"
        assert units_menu.execute()


def test_get_price(client):
    with client.session_transaction() as session:
        price_menu = BusinessPremisesRegistrationMenu(
            session=session, session_id="qwerty12345", user_response="500"
        )
        price_menu.session["level"] = 38
        assert price_menu.session.get("level") == 38
        assert price_menu.user_response == "500"
        assert price_menu.execute()


def test_get_alternate_contacts(client):
    with client.session_transaction() as session:
        contacts_menu = BusinessPremisesRegistrationMenu(
            session=session, session_id="qwerty12345", user_response="0788456790"
        )
        contacts_menu.session["level"] = 39
        assert contacts_menu.session.get("level") == 39
        assert contacts_menu.user_response == "0788456790"
        assert contacts_menu.execute()


def test_save_rental_biz_premises(client):
    with client.session_transaction() as session:
        rental_biz_premises = BusinessPremisesRegistrationMenu(
            session=session, session_id="qwerty12345", user_response="078945780"
        )
        rental_biz_premises.session["rent_out_biz_premises"] = "2"
        rental_biz_premises.session["level"] = 40
        for_rent = True
        assert rental_biz_premises.session.get("rent_out_biz_premises") == "2"
        assert for_rent
        assert rental_biz_premises.user_response == "078945780"
        assert rental_biz_premises.session.get("level") == 40
        assert rental_biz_premises.save_data()
        assert rental_biz_premises.execute()


def test_save_biz_premises_for_sale(client):
    with client.session_transaction() as session:
        biz_premises_for_sale = BusinessPremisesRegistrationMenu(
            session=session, session_id="qwerty12345", user_response="078945780"
        )
        for_rent = False
        biz_premises_for_sale.session["sell_business"] = "4"
        biz_premises_for_sale.session["level"] = 40
        assert biz_premises_for_sale.session.get("level") == 40
        assert not for_rent
        assert biz_premises_for_sale.user_response == "078945780"
        assert biz_premises_for_sale.session.get("sell_business") == "4"
        assert biz_premises_for_sale.save_data()
