from apscheduler.schedulers.background import BackgroundScheduler
from .update_db import *


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_db_sbd, 'interval', seconds=3600)
    # scheduler.add_job(update_db_sbd, 'interval', seconds=60)
    scheduler.add_job(update_db_gonets, 'interval', seconds=3600)
    # scheduler.add_job(update_db_gonets, 'interval', seconds=180)
    scheduler.add_job(update_db_html, 'interval', seconds=3600)
    # scheduler.add_job(update_db_html, 'interval', seconds=30)
    scheduler.start()
