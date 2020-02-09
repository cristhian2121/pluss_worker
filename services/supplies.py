import requests
from flask import json
from requests.exceptions import HTTPError

# 
from .db import CONECCION_DB
from utils.conversor import set_product, MPPROMOCIONALES

class Supplies_Service:

    _TOKEN = '04822d0d1e40429463a48c40bff430bf7874be23e304f44e3661bbc44e9e6b83'
    _URI = 'https://mppromocionales.com/ws_products.php'
    _HEADERS = {'content-type': 'application/json'}

    def get_products(self, supplier, provider):
        print('LLEGO')
        if MPPROMOCIONALES == provider:
            mppromocionales = supplier[provider]            
            uri = mppromocionales['URI']
            print('uri', uri)
            token = mppromocionales['TOKEN']
            print('token', token)
            response = requests.get(f'{uri}',  params = { 'token': token })
            if response.status_code == 200:
                response_json = response.json()
                print('Bien y en json')
                insert_products = self.saveProduct(response_json)
                if insert_products: print('Bien')
                else: print('MAL')
            else:            
                return {message: 'dont exist response', status: false, code: 500}
        else: return False
    
    def saveProduct(self, data):
        if data and len(data) > 0:
            # try:
                for item in data:               
                    product = set_product(item)
                    print(product['referency_id'])
                    exist = requests.get(CONECCION_DB, params={ 'referency_id': product['referency_id'] })       
                    product_list = exist.json()              
                    print('SI') if product_list['results'] else print('NO')
                    if not product_list['results']:
                        exist = None
                        try:
                            response = requests.post(CONECCION_DB, data=json.dumps(product), headers = self._HEADERS)
                            response.raise_for_status()
                        except HTTPError as http_err:
                            print(f'HTTP error INSERT: {http_err}')
                        except Exception as err:
                            print(f'Other error INSERT: {err}')
                    else:
                        product_dic = product_list['results'][0]
                        product_id = product_dic['id']
                        try:
                            response = requests.put(f'{CONECCION_DB}{product_id}/', data=json.dumps(product), headers = self._HEADERS)
                            response.raise_for_status()
                        except HTTPError as http_err:
                            print(f'HTTP error UPDATE: {http_err}')
                        except Exception as err:
                            print(f'Other error UPDATE: {err}')
                print('Success!')
                return True
        return False


# json.dumps serializer object json to json string strungFy

