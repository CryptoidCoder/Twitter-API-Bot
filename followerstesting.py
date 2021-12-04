#imports
import functions
import tweepy
import time
import requests
import schedule
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_key = os.getenv("API_key")
API_key_secret = os.getenv("API_key_secret")
Access_token = os.getenv("Access_token")
Access_token_secret = os.getenv("Access_token_secret")

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_key,API_key_secret)
auth.set_access_token(Access_token,Access_token_secret)

# Create API object
api = tweepy.API(auth)

me = os.getenv("my_username")



def checknewfollowers():
    global previous_followers_list
    global unfollowers_list
    unfollowers_list = [] #wipe unfollowers list    

    #get current follower list - save as changing variable new_followers_list
    new_followers_list = functions.getfollowers(me) #save the second set of followers in a list
    copy_new_followers_list = new_followers_list #duplicate new_followers_list
    copy_new_followers_list = list(copy_new_followers_list.split(", ")) #convert string to list
    new_followers_list = list(new_followers_list.split(", ")) #convert string to list
    #previous_followers_list = list(previous_followers_list.split(", ")) #convert string to list

    for user in previous_followers_list: #for each user in previous list remove them from new list, if it doesnt work then they have unfollowed
        try:
            new_followers_list.remove(user)
        except:
            unfolloweduser = f"{user}"
            unfollowers_list.append(unfolloweduser)


    print()
    if unfollowers_list == None or unfollowers_list == 'None':
        unfollowers_list == []

    if unfollowers_list == [] and new_followers_list == []:
        print(f"{datetime.now().strftime('%H:%M:%S')} - Account Stayed The Same.")
    elif unfollowers_list != []:
        for user in unfollowers_list:
            print(f"{datetime.now().strftime('%H:%M:%S')} - {user} unfollowed you :(")
            functions.tweet(f"So Sorry To see You Go @{user} :( 👋")
    elif new_followers_list != []:
        for user in new_followers_list:
            print(f"{datetime.now().strftime('%H:%M:%S')} - {new_followers_list} followed you :))")
            functions.tweet(f"Yay, Welcome To The Gang @{user} 👋,\n To See My Work Visit https://github.com/CryptoidCoder/")

    previous_followers_list = copy_new_followers_list #set previous as the current for next time





schedule.every(1).minutes.do(checknewfollowers) #every minute check for new followers

print(f"Checking For New Followers @ {datetime.now().strftime('%H:%M:%S')}")# original logging

#get current follower list - save as static variable original_followers_list
original_followers_list = functions.getfollowers(me) #save the first set of followers in a list
print(f"{datetime.now().strftime('%H:%M:%S')} Original Followers: {original_followers_list}") #printout the followers as of the start of the function

#duplicate into a changing variable - previous_followers_list
previous_followers_list = original_followers_list
previous_followers_list = list(previous_followers_list.split(", ")) #convert string to list

unfollowers_list = []

while True:
    schedule.run_pending() #start all functions scheduled
    time.sleep(1) #sleep