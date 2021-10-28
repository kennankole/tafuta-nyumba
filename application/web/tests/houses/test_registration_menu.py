from app.houses.registration import HousesRegistrationMenu

def test_houses_registration_consent_agree(client):
    with client.session_transaction() as session:
        reg_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response="1"
        )
        reg_menu.session['level'] = 30
        assert reg_menu.session.get("level") == 30
        # assert reg_menu.get_registration_consent()
        assert reg_menu.execute()

def test_houses_registration_consent_decline(client):
    with client.session_transaction() as session:
        reg_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response="2"
        )
        reg_menu.session['level'] = 31
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

        
def test_get_county(client):
    with client.session_transaction() as session:
        county_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response=""
        )
        county_menu.session['level'] = 31
        assert county_menu.session.get('level') == 31
        assert county_menu.execute()


def test_get_constituency(client):
    with client.session_transaction() as session:
        const_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response=""
        )
        const_menu.session['level'] = 32
        assert const_menu.session.get('level') == 32
        assert const_menu.execute()

def test_get_ward(client):
    with client.session_transaction() as session:
        ward_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response=""
        )
        ward_menu.session['level'] = 33
        assert ward_menu.session.get('level') == 33
        assert ward_menu.execute()   


def test_get_estate_village(client):
    with client.session_transaction() as session:
        village_estate_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response=""
        )
        village_estate_menu.session['level'] = 34
        assert village_estate_menu.session.get('level') == 34
        assert village_estate_menu.execute()    

def test_get_units(client):
    with client.session_transaction() as session:
        units_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response=""
        )
        units_menu.session['level'] = 35
        assert units_menu.session.get('level') == 35
        assert units_menu.execute() 

def test_get_price(client):
    with client.session_transaction() as session:
        price_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response="2"
        )
        price_menu.session['level'] = 36
        assert price_menu.session.get('level') == 36
        assert price_menu.user_response == "2"
        assert price_menu.execute()

def test_get_alternate_contacts(client):
    with client.session_transaction() as session:
        contacts_menu = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response="8000"
        )
        contacts_menu.session['level'] = 37
        assert contacts_menu.session.get('level') == 37
        assert contacts_menu.user_response == "8000"
        assert contacts_menu.execute()

def test_save_rental_houses(client):
    with client.session_transaction() as session:
        rental_houses = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response="0789234567"
        )
        rental_houses.session['level'] = 38
        rental_houses.session['rent_out_house'] = "2"
        assert rental_houses.session.get('level') == 38
        assert rental_houses.user_response == "0789234567"
        assert rental_houses.session.get("rent_out_house") == "2"
        assert rental_houses.execute()

def test_save_houses_for_sale(client):
    with client.session_transaction() as session:
        houses_for_sale = HousesRegistrationMenu(
            session=session,
            session_id="qwerty12345",
            user_response="0789234567"
        )
        houses_for_sale.session['sell_house'] = "4"
        houses_for_sale.session['level'] = 38
        assert houses_for_sale.user_response == "0789234567"
        assert houses_for_sale.session.get('level') == 38
        assert houses_for_sale.session.get("sell_house") == "4"
        assert houses_for_sale.execute()

