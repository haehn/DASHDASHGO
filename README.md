# DASHDASHGO
A simple framework to listen to Amazon Dash IoT events.

Run the server and configure your actions in _dashdashgo.py_.

Use the following Python 2.7 AWS lambda code:

```python
from __future__ import print_function

import base64
import json
import urllib2

print('Loading function')


def lambda_handler(event, context):

    server = 'http://DASHDASHGO_IP:2001' # CHANGE HERE

    urllib2.urlopen(server+'/knopf/'+base64.b64encode(json.dumps(event)))

    return True
```
