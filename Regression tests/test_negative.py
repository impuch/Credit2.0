import requests
import json
import jsonpath
import pytest

@pytest.mark.regression
def test_credit_auth():
    global token_value
    global auth
    Api_url = "https://credit-api-stage.apps.data-axle.com/api/v1/login/"
    f= open('C:/Users/impuch/PycharmProjects/Credit2.0/Testdata/nocredit.json')
    json_request = json.loads(f.read())
    session = requests.Session()
    response = session.post(Api_url, json=json_request, verify=False)
    assert response.status_code == 200
    print(f"\nToken: {response.content}")
    token_value = jsonpath.jsonpath(response.json(), 'token')
    auth = {"Authorization": "Bearer " + token_value[0]}
    print('token:', token_value)


@pytest.mark.regression
def test_Search_Bus_Detail():
    #param={'id':"433728707/"}
    id = '433728707'
    response = requests.get('https://credit-api-stage.apps.data-axle.com/api/v1/search/business/detail/'+ id,headers=auth, verify=False)
    assert response.status_code == 402
    print(response.text)
    print(response.url)

@pytest.mark.regression
def test_Search_Bus_nearby():
    id = '433728707'
    response = requests.get('https://credit-api-stage.apps.data-axle.com/api/v1/search/business/nearby/'+id, headers=auth, verify=False)
    assert response.status_code == 200
    print(response.text)