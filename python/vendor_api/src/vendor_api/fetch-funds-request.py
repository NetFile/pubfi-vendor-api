import requests
from requests.auth import HTTPBasicAuth

from config import read_config

try:
    config = read_config()

    headers = {'Accept': 'application/json'}
    basicAuth = HTTPBasicAuth(config.vendorKey, config.vendorSecret)
    params = {
       'filerAuthId': config.filerAuthId,
       'filerAuthPassword': config.filerAuthPassword,
    }
    url = f"{config.baseUrl}/requests/{config.filingId}"

    response = requests.get(url, auth=basicAuth, headers=headers, params=params)

    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
    print(f'Status Code: {response.status_code}')
    print(f'Response JSON: {response.json()}')
except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')