import tweepy
import time
from functions import *

myfollowers = []

for i in range(3):
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow() # follow them back
        if follower.screen_name in myfollowers: #if they are already in list then do nothing for 60 secs
            #print("No new followers")
            time.sleep(60)
        else:
            myfollowers.append(follower.screen_name) # if they are new then add them to the list
            #print("new followers:")
            print(myfollowers)
            #tweet("Thanks for the follow @" + follower.screen_name") #tweet a message
            time.sleep(60)
