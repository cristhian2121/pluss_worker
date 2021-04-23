from flask import Flask, request

# Services
from services.supplies import Supplies_Service
# from services.crons import init_cron
from services.provider import Provider

# Utils
from utils.conversor import MARPICO

app = Flask(__name__)
supplies_service = Supplies_Service()

mmpromocionales = Provider()

# init_cron()

@app.route('/sync/<key>', methods=['GET'])
def test_call(key):
    user_ip = request.remote_addr
    print('request.args')
    if key == 'cris' :
        response = supplies_service.get_products(MARPICO)
        if response: return 'ok'
        return f'Im runming {user_ip}'
    return 'You dont have access to this site'
