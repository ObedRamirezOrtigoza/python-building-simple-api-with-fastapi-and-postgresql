import requests

#response = requests.get('http://127.0.0.1:8000')
#print(response.json())

import requests

print(requests.get('http://127.0.0.1:8000/stock/AMZN').json())
#{'symbol': 'AMZN', 'stockname': 'Amazon.com Inc. Common Stock', 'lastsale': '$146.74', 'country': 'United States', 'ipoyear': 1997}
