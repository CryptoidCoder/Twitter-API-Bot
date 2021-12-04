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


def comparelists(word_list, removal_list): #comparelists(current_followers, old_followers)
    global newfollowerslist
    newfollowerslist = None #wipe new follower list
    for word in removal_list: #remove each word in removal_list from word_list
        word_list.remove(word)
    newfollowerslist = word_list
        
    return word_list

#PsuedoCode for checking if any new followers:
def checknewfollowers():
    #sort out variables /strings / lists
    global current_followers #make changes to current_followers globally
    global new_followers #make changes to new_followers globally
    current_followers = list(current_followers.split(", ")) #convert string to list
    
    new_followers = functions.getfollowers(me) #get new updated list of followers
    new_followers = list(new_followers.split(", ")) #convert string to list

    comparelists(new_followers, current_followers)
    current_followers = new_followers #make the current "new followers" list into the "old followers list"
    if newfollowerslist != None: #if there are new followers
        print(f"New Users Following me = {newfollowerslist}")
        for new_follower in newfollowerslist: #for each new follower shout them out in a tweet
            functions.tweet(f"Welcome @{new_follower} to the {me} Twitter Page - Thanks For The Follow")


#schedule.every().day.at("12:30").do(tweet) #at 12:30 every day tweet a message
schedule.every().day.at("12:30").do(functions.tweetfromque)
schedule.every(1).minutes.do(checknewfollowers) #every 2 minutes check if new followers

print(datetime.now().strftime("%H:%M:%S"))
current_followers = functions.getfollowers(me) #save the first set of followers in a list
while True:
    schedule.run_pending() #start all functions scheduled
    time.sleep(1) #sleep