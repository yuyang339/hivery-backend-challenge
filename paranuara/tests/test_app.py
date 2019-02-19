import falcon
from falcon import testing
import pytest
import falcon.status_codes as status
from mock import patch
from paranuara.app import ParanuaraService
from paranuara.resources import company, people, friend


@pytest.fixture()
def client():
    # Assume the hypothetical `myapp` package has a function called
    # `create()` to initialize and return a `falcon.API` instance.
    return testing.TestClient(ParanuaraService.create())

def test_wrong_route(client):
    # no route matches the request
    resp = client.simulate_get('/unexisting_route')
    assert resp.status == status.HTTP_404

def test_company_route(client):
    with patch("paranuara.resources.company.CompanyController.getAllEmployees", return_value={}):
        resp = client.simulate_get('/api/company/22/employees')

    assert resp.status == status.HTTP_200

    with patch("paranuara.resources.company.CompanyController.getAllEmployees", return_value={}):
        # no route matches the request
        resp = client.simulate_get('/api/company/employees')

    assert resp.status == status.HTTP_404

def test_friend_route(client):
    with patch("paranuara.resources.friend.FriendController.getCommonFriends", return_value={}):
        # Catch invalid query string
        resp = client.simulate_get('/api/commonfriend/2/1', query_string='ddd=a')

        assert resp.status == status.HTTP_400
        assert resp.json == {
            "title": "Please provide valid query ['isalive', 'eyecolor']"
        }
