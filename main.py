# import views.view

# # if __name__ == '__main__':
# #     app.run(debug=True, host='0.0.0.0')

from flask import Flask, request

from services.supplies import Supplies_Service
from services.crons import init_cron
from config import config
from utils.conversor import MPPROMOCIONALES
from services.provider import Provider

app = Flask(__name__)
supplies_service = Supplies_Service()

mmpromocionales = Provider()

init_cron()

@app.route('/sync/<key>', methods=['GET'])
def test_call(key):
    user_ip = request.remote_addr
    print('request.args')
    if key == 'cris' :
        response = supplies_service.get_products(config, MPPROMOCIONALES)
        if response: return 'ok'
        return f'Im runming {user_ip}'
    return 'You dont have access to this site'
