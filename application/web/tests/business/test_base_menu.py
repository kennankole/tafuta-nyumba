from app.business.biz_base_menu import BusinessPremisesMainMenu


def test_business_premises_rent(client):
    with client.session_transaction() as session:
        rent_biz_menu = BusinessPremisesMainMenu(
            session=session, session_id="qwerty123", user_response="1"
        )
        assert rent_biz_menu.business_premises_services_menu()


def test_business_premises_rent_out(client):
    with client.session_transaction() as session:
        rent_biz_menu = BusinessPremisesMainMenu(
            session=session, session_id="qwerty123", user_response="2"
        )
        assert rent_biz_menu.business_premises_services_menu()


def test_business_premises_sell(client):
    with client.session_transaction() as session:
        rent_biz_menu = BusinessPremisesMainMenu(
            session=session, session_id="qwerty123", user_response="3"
        )
        assert rent_biz_menu.business_premises_services_menu()


def test_business_premises_buy(client):
    with client.session_transaction() as session:
        rent_biz_menu = BusinessPremisesMainMenu(
            session=session, session_id="qwerty123", user_response="4"
        )
        assert rent_biz_menu.business_premises_services_menu()


def test_business_premises_services_invalid_input(client):
    with client.session_transaction() as session:
        rent_biz_menu = BusinessPremisesMainMenu(
            session=session, session_id="qwerty123", user_response=""
        )
        assert rent_biz_menu.business_premises_services_menu()


def test_business_premises_execute_menu(client):
    with client.session_transaction() as session:
        exec_menu = BusinessPremisesMainMenu(
            session=session, session_id="qwerty123", user_response=""
        )
        assert exec_menu.execute()
