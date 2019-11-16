import jwt
from datetime import datetime, timedelta
import time
import http.client
import json

conn = http.client.HTTPSConnection("api.zoom.us")
secret='5qiqwa29CVJxXkW4OQdMYLo75gH250Oy7Oyw'
key='bYLN1yTTQsKZsqstxxG3Pw'

exp = int(time.time()+300)
payload={ 'iss': '{}'.format(key), 'exp': '{}'.format(exp) }
header={ "alg": "HS256", "typ": "JWT" }
encoded_jwt = jwt.encode(payload, secret, algorithm='HS256', headers=header)

headers = {}
headers['User-Agent'] = 'Zoom-Jwt-Request'
headers['content-type'] = 'application/json'
headers['Authorization'] = 'Bearer '+encoded_jwt.decode('utf-8')

# headers is now ready to be used to make API calls...

conn.request("GET", "/v2/users?status=active&page_size=30&page_number=1", headers=headers)
res = conn.getresponse()
data = res.read()
out = data.decode("utf-8")
parsed = json.loads(out)
print(json.dumps(parsed, indent=4, sort_keys=True))

