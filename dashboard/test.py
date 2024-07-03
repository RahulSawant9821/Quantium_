import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def dash_app():
    from dashboard import Soul
    import Soul  # Import the app from app.py
    return Soul.app

def test_header(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element('h1')
    assert header.text == 'Sales of Soul Food Over Different Dates'

def test_visualisation(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    graph = dash_duo.find_element('#line-chart')
    assert graph is not None

def test_region_picker(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    radio_items = dash_duo.find_element('#region')
    assert radio_items is not None