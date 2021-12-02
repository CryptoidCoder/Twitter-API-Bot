#imports
import functions
import schedule
import time
from datetime import datetime

import os
from dotenv import load_dotenv

load_dotenv()
me = os.getenv("my_username")

#tweet a message
def tweet(): #tweet an automatic tweet message
    tweetmessage = f'This Is An Automagic Tweet From https://github.com/CryptoidCoder/Twitter-API-Bot/tree/cloudrun Running on Python Anywhere @ {datetime.now().strftime("%H:%M")}'
    print(f"Tweeting: {tweetmessage}")
    print()
    functions.tweet(tweetmessage)


def comparelists(firstlist, secondlist):
    global newfollowerslist
    newfollowerslist = None #wipe new follower list
    newfollowerslist = [i for i in secondlist if i not in firstlist]
    print(f"New Followers after conversion = {newfollowerslist}")
    #for follower in secondlist: #for each user in the current new followers list check if they were following last time it was checked
    #    if follower in firstlist: #if so then delete that user from both lists
    #        firstlist = firstlist.replace(follower,'')
    #        secondlist = secondlist.replace(follower,'')

    if secondlist == None: #if no new followers (new followers list = empty) send back message
        message = "Nothing left in secondlist(no new followers)"
    elif secondlist != None: #if new followers (new followers list != empty) send back message + list of users
        message = "New followers!"
        

    return message
    #return message, newfollowerslist

#PsuedoCode for checking if any new followers:
def checknewfollowers():
    global current_followers #make changes to current_followers globally
    global new_followers #make changes to new_followers globally
    #current_followers = None #wipe previous "old followers"
    new_followers = functions.getfollowers(me) #get new updated list of followers
    print(f"Old Followers = {current_followers}")
    print(f"New Followers = {new_followers}")
    #message,newfollowerslist = comparelists(current_followers, new_followers) #see if anyone new has followed you in the past hour
    print(comparelists(current_followers, new_followers))
    current_followers = new_followers#make the current "new followers" list into the "old followers list"
    if newfollowerslist != None: #if there are new followers
        print(f"New Users Following me = {newfollowerslist}")
        #for new_follower in newfollowerslist: #for each new follower shout them out in a tweet
            #functions.tweet(f"Welcome {new_follower} to the {me} Twitter Page - Thanks For The Follow")


#schedule.every().day.at("12:30").do(tweet) #at 12:30 every day tweet a message
schedule.every(1).minutes.do(checknewfollowers) #every 2 minutes check if new followers

print(datetime.now().strftime("%H:%M"))
current_followers = functions.getfollowers(me) #save the first set of followers in a list
print(f"Start: Current followers = {current_followers}")
while True:
    schedule.run_pending() #start all functions scheduled
    time.sleep(1) #sleep