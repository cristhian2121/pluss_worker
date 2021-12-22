from enviroment import env
from debugger import initialize_flask_server_debugger_if_needed

from flask import Flask, request
from multiprocessing import Process
from flask_crontab import Crontab
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
crontab = Crontab(app)
supplies_service = Supplies_Service()

@crontab.job(
    minute="10",
    hour="00"
)
def my_scheduled_job():
    """Cron job to update products"""
    now = datetime.now()
    time = now.strftime('%H:%M:%S')
    print("api call: {time}")
    r = requests.get(f'http://{config["IP_SERVER"]}:5000/sync/cris')
    # r = requests.get(f'http://localhost:5000') # test cron
    

@app.route('/', methods=['GET'])
def test():
    """Test endpoint"""
    print("yes")
    return "ok"



@app.route('/sync/<key>', methods=['GET'])
def test_call(key):
    user_ip = request.remote_addr
    print('request.args')
    if key == 'cris' :
        response = supplies_service.get_products(MARPICO)
        if response: return 'ok'
        return f'Im runing {user_ip}'
    return 'You dont have access to this site'
