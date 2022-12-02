# https://api.v2.emissions-api.org/ui/

import requests


url = 'https://api.v2.emissions-api.org'

endp = '/api/v2/countries.json'

endp1 = '/api/v2/products.json'


product = 'methane'
endp2 = '/api/v2/methane/average.json'

endpoint = f'{url}{endp}'
endpoint1 = f'{url}{endp1}'
endpoint2 = f'{url}{endp2}'

headers = {
    'Accept': 'application/json',
}

params = {
    'country': 'MK'
}
# response = requests.get(url=endpoint, headers=headers)

response = requests.get(url=endpoint2, headers=headers, params=params)
print(response.status_code)
print(response.json())
