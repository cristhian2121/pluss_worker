import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from flask import json
from requests.exceptions import HTTPError

# Config
from config import config

# 
from .db import CONECCION_DB
from utils.conversor import set_product, MARPICO

class Supplies_Service:

    _SESS = requests.Session()
    _RETRY = Retry(connect=50, backoff_factor=0.5)
    _ADAPTER = HTTPAdapter(max_retries=_RETRY)
    _SESS.mount('http://', _ADAPTER)

    _headers = { 'content-type': 'application/json' }

    def get_url(self, provider: str):
        providerAux = config[provider]
        if providerAux:
            uri = providerAux['URI']
            token = providerAux['TOKEN']
            if MARPICO == provider:
                self._headers['Authorization'] = f'Api-Key {token}'
                self._SESS.headers.update(self._headers)
            return uri
        return ''

    def get_products(self, provider): 
        url = self.get_url(provider)
        if url:
            response = self._SESS.get(url)
            if response.status_code == 200:
                response_json = response.json()
                insert_products = self.saveProduct(response_json["results"], provider)
                if insert_products: print('Bien')
                else: print('MAL')
            else:
                print('else')
                return dict(message='Error in our services, please try again',
                            status=False,
                            code=500)
        return dict(message='dont exist provider',
                        status=False,
                        code=401)

    def saveProduct(self, data, provider):
        if data and len(data) > 0:
            # try:
            for item in data:
                #extract data
                item.update({ "provider": provider })
                materiales = item["materiales"]
                for product_input in materiales:
                    if not product_input: continue
                    product_raw = item.copy()                    
                    product_raw.pop("materiales")
                    product_raw.update(product_input)
                    product = set_product(product_raw)
                    exist = requests.get(CONECCION_DB, params={'referency_id': product['referency_id']})
                    product_list = exist.json()
                    if not product_list['results']:
                        print('POST')
                        exist = None
                        try:
                            response = requests.post(CONECCION_DB,
                                                    data=product
                                                    )
                            response.raise_for_status()
                        except HTTPError as http_err:
                            print(f'HTTP error INSERT: {http_err}')
                        except Exception as err:
                            print(f'Other error INSERT: {err}')
                    else:
                        self.updateProduct(product_list, product)
            print('Success!')
            return True
        return False

    def updateProduct(self, product_from_db, newProduct):
        product_dic = product_from_db['results'][0]
        product_id = product_dic['id']
        try:
            response = requests.put(f'{CONECCION_DB}{product_id}/', data=newProduct)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error UPDATE: {http_err}')
        except Exception as err:
            print(f'Other error UPDATE: {err}')