import tweepy
import time
from functions import *


myfollowers = []
timestocheck = 3 #how man times it should check
timetosleep = 60 #time to sleep between checking for followers (this is in seconds)

for i in range(timestocheck):
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow() # follow them back
        if follower.screen_name in myfollowers: #if they are already in list then do nothing for 60 secs
            print("No new followers")
            time.sleep(timetosleep)
        else:
            myfollowers.append(follower.screen_name) # if they are new then add them to the list
            print("new followers:")
            print(myfollowers) 

            #tweet("Thanks for the follow @" + follower.screen_name") #tweet a message
            time.sleep(timetosleep)
