from enviroment import env
from debugger import initialize_flask_server_debugger_if_needed

from flask import Flask, request
from multiprocessing import Process
import requests
from datetime import datetime

# Services
from services.supplies import Supplies_Service
from services.provider import Provider

# Utils
from utils.conversor import MARPICO
from config import config

# comment to run sever amd latter uncomment for attach with Vscode
# initialize_flask_server_debugger_if_needed()

# debbugProcess = Process(target=initialize_flask_server_debugger_if_needed, args=())
# debbugProcess.start()
# debbugProcess.join()

app = Flask(__name__)
supplies_service = Supplies_Service()


@app.route('/', methods=['GET'])
def test():
    """Test endpoint"""
    print("yes")
    return "ok"


@app.route('/sync/<key>', methods=['GET'])
def test_call(key):
    user_ip = request.remote_addr
    print('request.args')
    if key == 'cris':
        response = supplies_service.get_products(MARPICO)
        if response:
            return 'ok'
        return f'Im runing {user_ip}'
    return 'You dont have access to this site'
