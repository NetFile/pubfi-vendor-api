# PubFi Vendor API

Documentation and Python samples which demonstrate PubFi Funds Request calls available to the Vendor including submission of attachments.

## Vendor Setup

1. Obtain Vendor Pin and API Credentials from NetFile Support.
1. Vendor provides callback URL (and credentials if necessary) which the NetFile PubFi system will use to submit messages to the Vendor.

## Vendor Process Overview

1. Vendor e-files Public Financing Filing (Matching or Qualifying).
1. NetFile processes the e-filing and creates a pending PubFi Funds Request.
1. NetFile sends HTTP POST with the Funds Request Received message to the callback URL of the vendor.
1. Vendor submits attachment for all supporting documentation.
1. Vendor submits Ready request to indicate all attachments have been submitted and the request is ready for processing.


## Messages Sent from NetFile to Vendor

All messages are sent as an HTTP POST to the URL provided by the vendor.

Three messages types are possible:

- ***Received*** - Sent on successful e-filing of a Matching or Qualifying request.
    - The vendor will submit attachments in response to this message, sending Ready when complete.
- ***Approved*** - Sent when the Funds Request has been approved by agency staff.
- ***Rejected*** - Sent when the Funds Request has been rejected by agency staff.

### Message Structure
MessageType property identifies the message type as enumerated above. Otherwise message structure is the same for all messages:

```json
{
    'messageType': 'Received',
    'efileContent': 'HDR..',
    'fundsRequest': {
        'filingId': '208608951',
        'requestStatus': 'Ready',
        'requestType': 'Qualifying',
        ...
    }
}
```

- messageType - Received, Approved, or Rejected
- efileContent - e-file content (csv)
- fundsRequest - the FundsRequest this messages relates to

## Requests Sent from Vendor to NetFile

PubFi API base url: http://netfile.com/Connect2/api/pubfi

All requests must include Vendor API credentials using Basic Authentication. 
Filer ID and Password are included in every request as filerAuthId and filerAuthPassword.

### Add Attachment

Submit AddAttachment request for each attachment/supporting document.
Provide the transactionId if the attachment is associated with a transaction.
Attachments without a transactionId will show as general supporting documentation on the Funds Request.

See 
[submit-attachment-multipart.py](python/vendor_api/src/vendor_api/submit-attachment-multipart.py) and
[submit-attachment-base64.py](python/vendor_api/src/vendor_api/submit-attachment-base64.py) 
for examples in Python.

> HTTP POST to /pubfi/requests/{filingId}/attachments

```json
{
    'filingId': '1234',
    'filerAuthId': 'ABC-999',
    'filerAuthPassword': 'secret',
    'transactionId': 'INC6',
    'fileName': 'proof.pdf', 
    'description': 'Proof',
    'contentType': 'application/pdf',
    'content': 'see note'
}
```
- filingId - filing ID from the e-filing process
- filerAuthId - filer id
- filerAuthPassword - filer password
- transactionId - id of the corresponding transaction (if not provided considered general supporting documentation)
- fileName - file name
- description - description of the attachment
- contentType - content or media type of the attachment
- content - attachment content can be provided as a file in a multipart request or as a Base64 encoded value assigned to this property

### Ready

Submit Ready when all attachments have been submitted and the funds request is Ready for agency approval.

See 
[submit-funds-request-ready.py](python/vendor_api/src/vendor_api/submit-funds-request-ready.py) for an example in Python.

> HTTP POST to /pubfi/requests/{filingId}/actions/ready

```json
{
    'filingId': '1234',
    'filerAuthId': 'ABC-999',
    'filerAuthPassword': 'secret',
    'performedBy': 'Human'
}
```
- filingId - filing ID from the e-filing process
- filerAuthId - filer id
- filerAuthPassword - filer password
- performedBy - informational for Vendor use (such as a user or system name)

## Python Examples
See 
[python/vendor_api/src/vendor_api](python/vendor_api/src/vendor_api) for Python examples

### Setup

1. Ensure you have Python installed (tested with 3.12).
1. Rename sample-config.yaml to config.yaml and provide required values.
1. Install dependencies.

From src:
```console
python -m pip install -r requirements.txt
```

### System Info
The sample [system-info.py](python/vendor_api/src/vendor_api/system-info.py) makes a simple HTTP GET request to PubFi, responding with current status message.
This can be useful for testing basic configuration and setup.

From src\vendor_api:
```console
python system-info.py
```