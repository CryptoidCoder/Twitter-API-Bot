#imports
import functions
import schedule
import time
from datetime import datetime

import os
from dotenv import load_dotenv

load_dotenv()
me = os.getenv("my_username")




#schedule.every().day.at("12:30").do(tweet) #at 12:30 every day tweet a message
schedule.every().day.at("18:44").do(functions.tweetfromque)
schedule.every(1).minutes.do(functions.checknewfollowers) #every 10 minutes check if new followers

print(f"Checking For New Followers @ {datetime.now().strftime('%H:%M:%S')}")# original logging
print(f"{datetime.now().strftime('%H:%M:%S')} Original Followers: {functions.original_followers_list}") #printout the followers as of the start of the function


unfollowers_list = []

while True:
    schedule.run_pending() #start all functions scheduled
    time.sleep(1) #sleep