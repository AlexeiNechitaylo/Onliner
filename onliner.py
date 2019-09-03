import pytest
from user_data import User_data
from app import App


@pytest.fixture()
def app(request):
	fixture = App()
	request.addfinalizer(fixture.destroy)
	return fixture


def test_onliner(app):
	app.login(User_data(email="ravlikgicel@gmail.com", password="6qwe1qwe"))
	app.click_cart()
	app.click_onliner_header()
	app.logout()