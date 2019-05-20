
from apscheduler.schedulers.background import BackgroundScheduler
import hub
import time

hub.Hub('scheduler').discoverRound()
timer = BackgroundScheduler(timezone='MST')
timer.add_job(hub.Hub('scheduler').discoverRound, trigger='interval', id='discover', minutes=5)
timer.start()

while True:
    a = 2
    time.sleep(5)
