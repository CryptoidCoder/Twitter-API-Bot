#imports
import functions
import schedule
import time
from datetime import datetime

import os
from os import environ

me = environ['my_username']


schedule.every().day.at("12:30").do(functions.tweetfromque) #at 12:30 every day tweet a message
schedule.every(10).minutes.do(functions.checknewfollowers) #every 10 minutes check if new followers

print(f"Checking For New Followers (File Initiated) @ {datetime.now().strftime('%H:%M:%S')}")# original logging

unfollowers_list = []

while True:
    schedule.run_pending() #start all functions scheduled
    time.sleep(1) #sleep