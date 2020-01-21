# from crontab import CronTab
# https://code.tutsplus.com/es/tutorials/managing-cron-jobs-using-python--cms-28231
# cron_mppromocionales = CronTab(user="root")
# cron_mppromocionales.new()}

# Libs
from datetime import datetime
# Services
from .supplies import Supplies_Service
from config import config
from utils.conversor import MPPROMOCIONALES

supplies_service = Supplies_Service()

def init_cron():
    print('_°_Init cron_°_')
    while True:
        now = datetime.now()
        time = now.strftime('%H:%M:%S')
        if time == '04:00:01':
            print(time)
            print(config[MPPROMOCIONALES])
            print('----------')
            res = supplies_service.get_products(config, MPPROMOCIONALES)



