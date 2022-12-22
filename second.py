import json

import requests


class EmissionsApi:
    """
    Class that contains methods to get responses from Emission API's endpoints.
    """

    def __init__(self, method, url, endpoint, headers, path_param=None, path=None, params=None):
        self.__method = method
        self.__url = url
        self.__endpoint = endpoint
        self.__headers = headers
        self.__path_param = path_param
        self.__path = path
        self.__params = params

    def request_no_body(self):
        url = f'{self.__url}{self.__endpoint}'
        headers = self.__headers
        if not isinstance(self.__headers, dict):
            raise Exception("Headers must be a dictionary.")
        # nacin 1
        # response = requests.get(url=url, headers=headers)
        response = self.__method(url=url, headers=headers)
        # print(response.status_code)
        return response.json()

    def request_with_path_parameters(self):
        url = f'{self.__url}{self.__endpoint}{self.__path_param}{self.__path}'
        headers = self.__headers
        if not isinstance(self.__headers, dict):
            raise Exception("Headers must be a dictionary.")
        if self.__params is not None:
            if not isinstance(self.__params, dict):
                raise Exception("Params must be a dictionary.")
            response = self.__method(url=url, headers=headers, params=params)
        else:
            response = self.__method(url=url, headers=headers)
        # print(response.status_code)
        return response.json()


url1 = 'https://api.v2.emissions-api.org'
endpoint1 = '/api/v2/countries.json'
headers1 = {
    'Accept': 'application/json'
}
ne_znam = EmissionsApi(requests.get, url1, endpoint1, headers1)
# nekoja_varijabla = ne_znam.request_no_body()
# print(nekoja_varijabla)

endpoint2 = '/api/v2/products.json'
vtor_endpoint = EmissionsApi(requests.get, url1, endpoint2, headers1)
# no_body_2 = vtor_endpoint.request_no_body()
# print(no_body_2)

endpoint3 = '/api/v2/'
path3_param = 'methane'
path3 = '/average.json'
params = {
    'country': 'MK',
    'limit': 5
}

tret_endpoint = EmissionsApi(requests.get, url1, endpoint3, headers1, path_param=path3_param, path=path3, params=params)
tret_povik = tret_endpoint.request_with_path_parameters()
# print(tret_povik)

path4_param = 'carbonmonoxide'
path4 = '/data-range.json'
cetvrt_endpoint = EmissionsApi(requests.get, url1, endpoint3, headers1, path_param=path4_param, path=path4)
cetvrt_povik = cetvrt_endpoint.request_with_path_parameters()
# print(cetvrt_povik)

path5_param = 'methane'
path5 = '/geo.json'
params5 = {
    'limit': 2
}
petti_endpoint = EmissionsApi(requests.get, url1, endpoint3, headers1, path_param=path5_param, params=params5, path=path5)
petti_povik = petti_endpoint.request_with_path_parameters()
# print(petti_povik)

path6_param = 'ozone'
path6 = '/statistics.json'
params6 = {
    'limit': 2,
    'country': 'MK'
}
sesti_endpoint = EmissionsApi(requests.get, url1, endpoint3, headers1, path_param=path6_param, params=params6, path=path6)
sesti_povik = sesti_endpoint.request_with_path_parameters()
# print(sesti_povik)
# with open('example.json', 'w') as f1:
#     f1.write(json.dumps(sesti_povik))