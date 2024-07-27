import base64
import json
import os

import requests
from requests.auth import HTTPBasicAuth

from config import read_config

try:
    config = read_config()

    basicAuth = HTTPBasicAuth(config.vendorKey, config.vendorSecret)
    url = f"{config.baseUrl}/requests/{config.filingId}/attachments"

    baseName = "no-trx-20"
    description = f"{baseName} - No trx"
    fileName = f"{baseName}.pdf"
    addAttachment = {
        'filingId': config.filingId,
        'filerAuthId': config.filerAuthId,
        'filerAuthPassword': config.filerAuthPassword,
        'fileName': fileName,
        'description': description,
        'contentType': 'application/pdf',
        #'content': contentAsBase64
    }

    # jsonBody = json.dumps(addAttachment)
    # print('JSON:' + jsonBody)



    # Make the POST request
    #response = requests.post(url, files=files, data=data)

    # Make the POST request
    #response = requests.post(url, json=addAttachment, auth=basicAuth, headers=headers, files=files)
    #response = requests.post(url, data=addAttachment, files=files, auth=basicAuth, headers=headers)
    #response = requests.post(url, data=addAttachment, files=files, auth=basicAuth, headers=headers)
    #response = requests.post(url, data=addAttachment, auth=basicAuth, headers=headers)
    #response = requests.post(url, json=addAttachment, auth=basicAuth, headers=headers)
    #response = requests.post(url, data=addAttachment, auth=basicAuth, headers=headers, files=files)

    fileName = "../../attachments/supporting-doc-no-trx-ref.pdf"


    # File to be sent in the POST request
    # files = {
    #     'body': (None, json.dumps(addAttachment), 'application/json'),
    #     'file': ("some file.abc", open(fileName, 'rb'), 'application/pdf')
    # }
    files = {
        'file': ('somefile.pdf',open('../../attachments/supporting-doc-no-trx-ref.pdf', 'rb'))
    }


    #headers = {'Accept': 'application/json', 'ContentType': 'application/json'}
    #headers = {'Accept': 'application/json', 'ContentType': 'multipart/form-data'}
    headers = {'Accept': 'application/json'}
    #response = requests.post(url, json=addAttachment, auth=basicAuth, headers=headers, files=files)

    #data = {'key': 'value'}  # Additional data if required
    response = requests.post(url, data=addAttachment, files=files, auth=basicAuth, headers=headers)

    # with open(fileName, 'rb') as file:
    #     response = requests.post(url, data=addAttachment, files={'file': file}, auth=basicAuth, headers=headers)

    #print(r.content)


    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)

    # Close the file
    #files['file'].close()

    print(f'Status Code: {response.status_code}')
    print(f'Response TEXT: {response.text}')
    #print(f'Response JSON: {response.json()}')
except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
    print(f'Response text: {response.text}')
except Exception as err:
    print(f'Other error occurred: {err}')