from app.hostels.results import HostelsQueryResults

def test_search_hostels(client):
    with client.session_transaction() as session:
        results_menu = HostelsQueryResults(
            session=session,
            session_id="qwerty1235",
            user_response="1"
        )
        assert results_menu.hostels_query_results_by_constituency()
        assert results_menu.hostels_query_results_by_ward()
        assert results_menu.hostels_query_results_by_school_name()

def test_hostels_query_results_execute(client):
    with client.session_transaction() as session:
        exec_menu = HostelsQueryResults(
            session=session,
            session_id="qwerty123",
            user_response="Ruaraka"
        )
        assert exec_menu.execute()
