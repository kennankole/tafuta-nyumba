from app.houses.registration import HousesRegistrationMenu

def test_houses_registration_consent_agree(client):
    with client.session_transaction() as session:
        reg_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response="1"
        )
        assert reg_menu.get_registration_consent()

def test_houses_registration_consent_decline(client):
    with client.session_transaction() as session:
        reg_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response="2"
        )
        assert reg_menu.get_registration_consent()

def test_houses_rental_registration_consent_invalid_input(client):
    with client.session_transaction() as session:
        reg_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response=""
        )
        reg_menu.session['rent_out_house'] = "2"
        assert reg_menu.user_response not in ("1", "2")
        assert reg_menu.session.get("rent_out_house") == "2"
        assert reg_menu.get_registration_consent()

def test_houses_for_sale_registration_consent_invalid_input(client):
    with client.session_transaction() as session:
        reg_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response=""
        )
        reg_menu.session["sell_house"] = "4"
        assert reg_menu.user_response not in ("1", "2")
        assert reg_menu.session.get("sell_house") == "4"
        assert reg_menu.get_registration_consent()

        
def test_get_count(client):
    with client.session_transaction() as session:
        county_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response=""
        )
        assert county_menu.get_county()


def test_get_constituency(client):
    with client.session_transaction() as session:
        const_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response=""
        )
        assert const_menu.get_constituency()


def test_get_ward(client):
    with client.session_transaction() as session:
        ward_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response=""
        )
        assert ward_menu.get_ward()      


def test_get_estate_village(client):
    with client.session_transaction() as session:
        village_estate_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response=""
        )
        assert village_estate_menu.get_estate_village()    

def test_get_units(client):
    with client.session_transaction() as session:
        units_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response=""
        )
        assert units_menu.get_house_units()  

def test_get_price(client):
    with client.session_transaction() as session:
        price_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response=""
        )
        assert price_menu.get_price() 

def test_get_alternate_contacts(client):
    with client.session_transaction() as session:
        contacts_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response=""
        )
        assert contacts_menu.get_alternate_contacts() 

def test_save_rental_houses(client):
    with client.session_transaction() as session:
        rental_houses = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response=""
        )
        rental_houses.session['rent_out_house'] = "2"
        assert rental_houses.session.get("rent_out_house") == "2"
        assert rental_houses.save_data()

def test_save_houses_for_sale(client):
    with client.session_transaction() as session:
        houses_for_sale = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response=""
        )
        houses_for_sale.session['sell_house'] = "4"
        assert houses_for_sale.session.get("sell_house") == "4"
        assert houses_for_sale.save_data()

