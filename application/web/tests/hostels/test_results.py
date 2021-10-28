from app.hostels.results import HostelsQueryResults

def test_search_hostels_by_school_name(client):
    with client.session_transaction() as session:
        results_menu = HostelsQueryResults(
            session=session,
            session_id="qwerty1235",
            user_response="Dedan Kimathi University"
        )
        assert results_menu.execute()
        assert results_menu.hostels_query_results_by_school_name()

def test_hostels_query_results_execute(client):
    with client.session_transaction() as session:
        exec_menu = HostelsQueryResults(
            session=session,
            session_id="qwerty123",
            user_response="Ruaraka"
        )
        assert exec_menu.execute()
        assert exec_menu.hostels_query_results_by_constituency()

def test_search_hostels_by_constituency(client):
    with client.session_transaction() as session:
        results_menu = HostelsQueryResults(
            session=session,
            session_id="qwerty1234",
            user_response="Korogocho"
        )
        assert results_menu.hostels_query_results_by_ward()
        assert results_menu.execute()


