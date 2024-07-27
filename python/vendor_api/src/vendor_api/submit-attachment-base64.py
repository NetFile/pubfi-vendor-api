import base64

import requests
from requests.auth import HTTPBasicAuth

from config import read_config

try:
    config = read_config()

    headers = {'Accept': 'application/json', 'ContentType': 'application/json'}
    basicAuth = HTTPBasicAuth(config.vendorKey, config.vendorSecret)
    params = {
       'filerAuthId': config.filerAuthId,
       'filerAuthPassword': config.filerAuthPassword,
    }
    url = f"{config.baseUrl}/requests/{config.filingId}/attachments"

    # read file
    with open('../../attachments/supporting-doc-with-trx-ref.pdf', 'rb') as file:
          content = file.read()


    # Construct Add Attachment request
    baseName = "attach-20"
    description = f"{baseName} - desc"
    fileName = f"{baseName}.pdf"
    contentAsBase64 = base64.b64encode(content).decode()
    addAttachment = {
        'filingId': config.filingId,
        'transactionId': 'INC6',  # optional
        'filerAuthId': config.filerAuthId,
        'filerAuthPassword': config.filerAuthPassword,
        'fileName': fileName,
        'description': description,
        'contentType': 'application/pdf',
        'content': contentAsBase64
    }

    # Make the POST request
    response = requests.post(url, json=addAttachment, auth=basicAuth, headers=headers)

    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)

    print(f'Status Code: {response.status_code}')
    print(f'Response JSON: {response.json()}')
except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
    print(f'Response text: {response.text}')
except Exception as err:
    print(f'Other error occurred: {err}')