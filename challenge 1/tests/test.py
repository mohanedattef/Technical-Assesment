from nose.tools import assert_true
import requests

#Case testing
BASE_URL = "http://127.0.0.1:5000"
def Test_Requests():
    response = requests.get('%s/bids' % (BASE_URL))
    assert_true(response.ok)

def Test_Post():
    payload = {'petid': 5 , 'userid': 55 , 'value': 555}
    response = requests.post('%s/bids' % (BASE_URL), json=payload)
    assert_true(response.status_code == 200)


def Test_Badinput():
    payload = {'petid': 'tyrion lannister'}
    response = requests.post('%s/bids' % (BASE_URL), json=payload)
    print(response.status_code)
    assert_true(response.status_code == 400)