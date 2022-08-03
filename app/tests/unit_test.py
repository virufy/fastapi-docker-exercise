import requests 
import ast
import json
from typing import Dict

def assert_app_response_valid(response: requests.Response) -> Dict[str, str]:
    assert response.status_code == 200
    result = json.loads(response.text)
    assert result['error_code'] == 'everything_ok'
    return result

def test_predict():
    response = requests.post(
        'http://localhost:8000/predict', 
        json = {
            'age': 10
        },
    )
    parsed_response = assert_app_response_valid(response)
    