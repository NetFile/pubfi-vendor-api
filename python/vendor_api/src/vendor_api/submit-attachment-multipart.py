import requests
from requests.auth import HTTPBasicAuth

from config import read_config

try:
    config = read_config()

    headers = {'Accept': 'application/json'}
    basicAuth = HTTPBasicAuth(config.vendorKey, config.vendorSecret)
    url = f"{config.baseUrl}/requests/{config.filingId}/attachments"

    # Build the request
    baseName = "attach-10"
    description = f"{baseName} - description"
    fileName = f"{baseName}.pdf"
    addAttachment = {
        'filingId': config.filingId,
        'filerAuthId': config.filerAuthId,
        'filerAuthPassword': config.filerAuthPassword,
        'transactionId': 'INC6', # optional
        'fileName': fileName,
        'description': description,
        'contentType': 'application/pdf'
    }

    # POST attachment with file as multipart
    with open("../../attachments/supporting-doc-with-trx-ref.pdf", 'rb') as attachmentFile:
        files = {
            'file': attachmentFile
        }
        response = requests.post(url, data=addAttachment, files=files, auth=basicAuth, headers=headers)

        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        print(f'Status Code: {response.status_code}')
        print(f'Response TEXT: {response.text}')

except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
    print(f'Response text: {response.text}')
except Exception as err:
    print(f'Other error occurred: {err}')