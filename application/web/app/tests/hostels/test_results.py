from app.hostels.results import HostelsQueryResults
from app.models import Hostels
from mixer.backend.flask import mixer

def test_search_hostels_by_school_name(client):
    with client.session_transaction() as session:
        results_menu = HostelsQueryResults(
            session=session,
            session_id="qwerty1235",
            user_response="Dedan Kimathi University",
        )
        assert results_menu.execute()
        assert results_menu.hostels_query_results_by_school_name()


def test_hostels_query_results_execute(client):
    with client.session_transaction() as session:
        exec_menu = HostelsQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        assert exec_menu.execute()
        assert exec_menu.hostels_query_results_by_constituency()


def test_search_hostels_by_constituency(client):
    with client.session_transaction() as session:
        results_menu = HostelsQueryResults(
            session=session, session_id="qwerty1234", user_response="Korogocho"
        )
        assert results_menu.hostels_query_results_by_ward()
        assert results_menu.execute()
        
        
    
def test_hostels_const_1_results(client):
    with client.session_transaction() as session:
        const_menu = HostelsQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.blend(Hostels, constituency="Ruaraka")
        assert Hostels.get_const_hostels(const="Ruaraka")
        assert const_menu.hostels_query_results_by_constituency()
        
def test_hostels_const_2_results(client):
    with client.session_transaction() as session:
        const_menu = HostelsQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.cycle(3).blend(Hostels, constituency="Ruaraka")
        assert Hostels.get_const_hostels(const="Ruaraka")
        assert const_menu.hostels_query_results_by_constituency()
        
def test_hostels_const_0_results(client):
    with client.session_transaction() as session:
        const_menu = HostelsQueryResults(
            session=session, session_id="qwerty123", user_response="Ruaraka"
        )
        mixer.blend(Hostels)
        assert Hostels.get_const_hostels(const="Ruaraka")
        assert const_menu.hostels_query_results_by_constituency()
        
        
def test_hostels_ward_2_results(client):
    with client.session_transaction() as session:
        const_menu = HostelsQueryResults(
            session=session, session_id="qwerty123", user_response="Korogocho"
        )
        mixer.cycle(3).blend(Hostels, ward="Korogocho")
        assert Hostels.query.filter_by(ward="Korogocho").count() > 2
        assert Hostels.get_ward_hostels(ward="Korogocho")
        assert const_menu.hostels_query_results_by_ward()
        
def test_hostels_ward_1_results(client):
    with client.session_transaction() as session:
        const_menu = HostelsQueryResults(
            session=session, session_id="qwerty123", user_response="Korogocho"
        )
        mixer.blend(Hostels, ward="Korogocho")
        assert Hostels.get_ward_hostels(ward="Korogocho")
        assert const_menu.hostels_query_results_by_ward()
        
def test_hostels_ward_0_results(client):
    with client.session_transaction() as session:
        const_menu = HostelsQueryResults(
            session=session, session_id="qwerty123", user_response="Korogocho"
        )
        mixer.blend(Hostels)
        assert Hostels.get_ward_hostels(ward="Korogocho")
        assert const_menu.hostels_query_results_by_ward()
           
        
def test_hostels_name_of_schools_1(client):
    with client.session_transaction() as session:
        const_menu = HostelsQueryResults(
            session=session, session_id="qwerty123", user_response="Dedan Kimathi University"
        )
        
        mixer.blend(Hostels,school_name="Dedan Kimathi University")
        assert Hostels.get_hostels_school_name(name="Dedan Kimathi University")
        assert const_menu.hostels_query_results_by_school_name()
        
 
def test_hostels_name_of_school_2_results(client):
    with client.session_transaction() as session:
        const_menu = HostelsQueryResults(
            session=session, session_id="qwerty123", user_response="Dedan Kimathi University"
        )
        mixer.cycle(3).blend(Hostels, school_name="Dedan Kimathi University")
        assert Hostels.query.filter_by(school_name="Dedan Kimathi University").count() > 2
        assert Hostels.get_hostels_school_name(name="Dedan Kimathi University")
        assert const_menu.hostels_query_results_by_school_name()
        
                
def test_hostels_name_of_school_0_results(client):
    with client.session_transaction() as session:
        const_menu = HostelsQueryResults(
            session=session, session_id="qwerty123", user_response="Dedan Kimathi University"
        )
        mixer.blend(Hostels)
        assert Hostels.get_hostels_school_name(name="Dedan Kimathi University")
        assert const_menu.hostels_query_results_by_school_name()
