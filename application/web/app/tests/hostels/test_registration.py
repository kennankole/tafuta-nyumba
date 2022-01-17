from app.hostels.registration import HostelsRegistrationMenu


def test_hostel_registration_consent_agree(client):
    with client.session_transaction() as session:
        menu = HostelsRegistrationMenu(
            session=session, session_id="qwerty1234", user_response="1"
        )
        menu.session["level"] = 90
        assert menu.session.get("level") == 90
        assert menu.execute()


def test_hostel_registration_consent_decline(client):
    with client.session_transaction() as session:
        menu = HostelsRegistrationMenu(
            session=session, session_id="qwerty1234", user_response=""
        )
        menu.session["level"] = 90
        assert menu.session.get("level") == 90
        assert menu.execute()


def test_hostel_registration_invalid_input(client):
    with client.session_transaction() as session:
        menu = HostelsRegistrationMenu(
            session=session, session_id="qwerty1234", user_response="2"
        )
        menu.session["level"] = 90
        assert menu.session.get("level") == 90
        assert menu.execute()


def test_get_county(client):
    with client.session_transaction() as session:
        county_menu = HostelsRegistrationMenu(
            session=session, session_id="qwerty12945", user_response="00"
        )
        county_menu.session["level"] = 91
        assert county_menu.session.get("level") == 91
        assert county_menu.execute()


def test_get_constituency(client):
    with client.session_transaction() as session:
        const_menu = HostelsRegistrationMenu(
            session=session, session_id="qwerty12945", user_response="Nairobi"
        )
        const_menu.session["level"] = 92
        assert const_menu.session.get("level") == 92
        assert const_menu.execute()


def test_get_ward(client):
    with client.session_transaction() as session:
        ward_menu = HostelsRegistrationMenu(
            session=session, session_id="qwerty12945", user_response="Ruaraka"
        )
        ward_menu.session["level"] = 93
        assert ward_menu.session.get("level") == 93
        assert ward_menu.execute()


def test_get_name_of_college_or_university(client):
    with client.session_transaction() as session:
        village_estate_menu = HostelsRegistrationMenu(
            session=session, session_id="qwerty12945", user_response="Korogocho"
        )
        village_estate_menu.session["level"] = 94
        assert village_estate_menu.session.get("level") == 94
        assert village_estate_menu.execute()


def test_get_units(client):
    with client.session_transaction() as session:
        units_menu = HostelsRegistrationMenu(
            session=session,
            session_id="qwerty12945",
            user_response="Dedan Kimathi Univeristy",
        )
        units_menu.session["level"] = 95
        assert units_menu.session.get("level") == 95
        assert units_menu.execute()


def test_get_price(client):
    with client.session_transaction() as session:
        price_menu = HostelsRegistrationMenu(
            session=session, session_id="qwerty12945", user_response="50"
        )
        price_menu.session["level"] = 96
        assert price_menu.session.get("level") == 96
        assert price_menu.execute()


def test_get_alternate_contacts(client):
    with client.session_transaction() as session:
        contacts_menu = HostelsRegistrationMenu(
            session=session, session_id="qwerty12945", user_response="8000"
        )
        contacts_menu.session["level"] = 97
        assert contacts_menu.session.get("level") == 97
        assert contacts_menu.execute()


def test_save_hostels(client):
    with client.session_transaction() as session:
        rental_hostels = HostelsRegistrationMenu(
            session=session, session_id="qwerty12945", user_response="0789456789"
        )
        rental_hostels.session["level"] = 98
        rental_hostels.session['price'] = 50
        rental_hostels.session['units'] = 5
        assert rental_hostels.session.get("level") == 98
        assert rental_hostels.execute()
