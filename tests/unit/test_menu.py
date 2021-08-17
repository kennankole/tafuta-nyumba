from logging import Manager
from app.menu.base_menu import Menu

def test_main_menu(client):
    with client.session_transaction() as session:
        main_menu = Menu(
            session_id="340990aareqo34",
            session = session,
            user_response="3",
        )
        assert main_menu.session == session
        assert main_menu.session_id == "340990aareqo34"
    assert main_menu.ussd_continue(main_menu.user_response)
    assert main_menu.ussd_end(main_menu.user_response)
    assert main_menu.home_menu()


    