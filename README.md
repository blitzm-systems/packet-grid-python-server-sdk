# Packet Grid Python Server SDK

- API version: 1.0.0
- Package version: 0.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/blitzm-systems/packet-grid-python-server-sdk.git

```
or
```sh
pipenv install -e git+https://github.com/blitzm-systems/packet-grid-python-server-sdk.git#egg=blitzm_packetgrid_sdk
```

```python
import blitzm_packetgrid_sdk 
```


## Getting Started
### send notifications



```python

from blitzm_packetgrid_sdk import Recipient, SendNotification, TransportEnum
from blitzm_packetgrid_sdk.services.packetgrid import PacketGrid


tenant_id = "Your tenant id from PacketGrid"
api_key = "Your PackerGrid API key"
# True or False depends on whether you would like to use the production mode
is_production = False  
packet_grid = PacketGrid(tenant_id, api_key, is_production)
recipient = Recipient(username='Recipient-unique-user-id',  # This is the id for searching notification reports of this recipient.
                      email='Recipient-email',
                      phone='Recipient-phone-number')
notification = SendNotification(title='Your-message-title',
                                detail='Your-detail',
                                recipients=[recipient],  # note: You can have multiple recipients
                                transports=[TransportEnum.EMAIL, TransportEnum.SMS],  # see below
                                payload={})
packet_grid.notifications.send(notification)

```
There are 3 types of transport channels: email, sms and fcm from  the `TransportEnum` model.





