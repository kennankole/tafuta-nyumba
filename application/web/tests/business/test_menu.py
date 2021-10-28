from app.business.menu import BusinessPremisesQueryMainMenu

def test_search_rental_business_premises(client):
    with client.session_transaction() as session:
        rent_query_menu = BusinessPremisesQueryMainMenu(
            session=session,
            session_id="qwerty1234",
            user_response="1"
        )
        assert rent_query_menu.user_response in ("1", "2", "3", "4")
        assert rent_query_menu.search_rental_business_premises()

    
def test_register_rental_business_premises(client):
    with client.session_transaction() as session:
        rental_biz_reg_menu = BusinessPremisesQueryMainMenu(
            session=session,
            session_id="qwerty123",
            user_response="5"
        )
        assert rental_biz_reg_menu.user_response in ("5", "6", "7", "8")
        assert rental_biz_reg_menu.register_rental_business_premises()


def test_register_business_premises_for_sale(client):
    with client.session_transaction() as session:
        sell_biz_reg_menu = BusinessPremisesQueryMainMenu(
            session=session,
            session_id="qwerty1234",
            user_response="50"
        )
        assert sell_biz_reg_menu.user_response in ("50", "60", "70", "80")
        assert sell_biz_reg_menu.register_business_premises_for_sale()


def test_search_business_premises_for_sale(client):
    with client.session_transaction() as session:
        buy_biz_premises = BusinessPremisesQueryMainMenu(
            session=session,
            session_id="qwerty12345",
            user_response="10"
        )
        assert buy_biz_premises.user_response in ("10", "20", "30", "50")
        assert buy_biz_premises.search_business_premises_for_sale()
        
def test_execute_menu(client):
    with client.session_transaction() as session:
        execute_menu = BusinessPremisesQueryMainMenu(
            session_id="qerq4234qdfaf",
            session=session,
            user_response="50"
        )
        assert execute_menu.execute()