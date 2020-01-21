import requests
from flask import json
from requests.exceptions import HTTPError

# 
from .db import CONECCION_DB
from utils.conversor import set_product, MPPROMOCIONALES

class Supplies_Service:

    _TOKEN = '04822d0d1e40429463a48c40bff430bf7874be23e304f44e3661bbc44e9e6b83'
    _URI = 'https://mppromocionales.com/ws_products.php'

    def get_products(self, supplier, provider):
        if MPPROMOCIONALES == provider:
            mppromocionales = supplier[provider]            
            uri = mppromocionales['URI']
            print('uri', uri)
            token = mppromocionales['TOKEN']
            print('token', token)
            response = requests.get(f'{uri}',  params = { 'token': token })
            if response.status_code == 200:
                response_json = response.json()
                insert_products = self.saveProduct(response_json)
                if insert_products:
                    print('Bien')
                    return True
                else: print('MAL')
            else:            
                return {message: 'dont exist response', status: false, code: 500}
        else: return False
    
    def saveProduct(self, data):
        if data and len(data) > 0:
            try:
                for item in data:               
                    product = set_product(item)
                    response = requests.post(CONECCION_DB, data=json.dumps(product), headers = {'content-type': 'application/json'})
                    response.raise_for_status()
                print('Success!')
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')  # Python 3.6
            except Exception as err:
                print(f'Other error occurred: {err}')  # Python 3.6
            return True
        return False

