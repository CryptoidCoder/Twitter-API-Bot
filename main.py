#imports
from functions import *
import schedule
import time
from datetime import datetime


#tweet a message
def tweet():
    tweetmessage = f"This Is An Automagic Tweet @ {datetime.now()}"
    print(f"Tweeting {tweetmessage}")
    tweet(tweetmessage)


def comparelists(firstlist, secondlist):
    newfollowers = None
    for follower in secondlist: #for each user in the current new followers list check if they were following last time it was checked
        if follower in firstlist: #if so then delete that user from both lists
            firstlist = firstlist.replace(follower,'')
            secondlist = secondlist.replace(follower,'')
    
    if secondlist == None: #if no new followers (new followers list = empty) send back message
        message = "Nothing left in secondlist(new followers)"
    elif secondlist != None: #if new followers (new followers list != empty) send back message + list of users
        message = "New followers!"
        secondlist = newfollowers
        
    return message, newfollowers

#PsuedoCode for checking if any new followers:
def checknewfollowers():
    old_followers = None
    current_followers = old_followers #set correct variable name for previous 10 minute list of followers
    current_followers = getfollowers(me) #get new updated list of followers
    message,newfollowers = comparelists(old_followers, current_followers) #see if anyone new has followed you in the past hour
    if newfollowers != None: #if there are new followers
        for new_follower in newfollowers: #for each new follower shout them out in a tweet
            tweet(f"Welcome {new_follower} to the CryptoidCoder Twitter Page - Thanks For The Follow")


schedule.every().day.at("12:30").do(tweet) #at 12:30 every day tweet a message
#schedule.every(10).minutes.do(checknewfollowers) #every 10 minutes chekc if new followers

#current_followers = getfollowers(me) #save the first set of followers in a list
while True:
    schedule.run_pending() #start all fucnitons scheduled
    time.sleep(1) #sleep