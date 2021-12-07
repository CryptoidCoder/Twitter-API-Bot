import tweepy
import requests
import os
from datetime import datetime



API_key = os.environ['API_key']
API_key_secret = os.environ['API_key_secret']
Access_token = os.environ['Access_token']
Access_token_secret = os.environ['Access_token_secret']

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_key,API_key_secret)
auth.set_access_token(Access_token,Access_token_secret)

# Create API object
api = tweepy.API(auth)

me = os.environ['my_username']




#get recipient id
def recipientid(user):
    user = api.get_user(screen_name=user)
    recipientid = user.id
    return recipientid

#print authors from tweets in timeline
def timeline():
    # This code snippet prints the author and text of the last tweets in your home timeline:
    timeline = api.home_timeline()
    for tweet in timeline:
        print(f"{tweet.user.name} said {tweet.text}")

#tweet a test message
def tweettestmessage(): #tweet an automatic tweet message
    tweetmessage = f'This Is An Automagic Tweet From https://github.com/CryptoidCoder/Twitter-API-Bot/tree/cloudrun Running on Python Anywhere @ {datetime.now().strftime("%H:%M")}'
    print(f"{datetime.now().strftime('%H:%M:%S')} : Tweeting: {tweetmessage}")
    print()
    tweet(tweetmessage)

#tweet a text-only message
def tweet(text):
    # The following code uses Tweepy to create a tweet with some text:
    api.update_status(status=text)
    print(f"{datetime.now().strftime('%H:%M:%S')} : Tweeting: {text}")

#tweets message with image
def tweetimage(pathtoimage, text):
    api.update_status_with_media(filename=pathtoimage,status=text)
    print(f"{datetime.now().strftime('%H:%M:%S')} : Tweeting: {tweetmessage} + Image: {pathtoimage}")

#tweets message with image url
def tweetimagewithurl(imageurl, text):
    mediapath = '.\\images\\animage.png'
    myfile = requests.get(imageurl)
    open(mediapath, 'wb').write(myfile.content)
    uploadedmedia = api.media_upload(filename=mediapath)
    api.update_status_with_media(filename=mediapath,status=text)
    print(f"{datetime.now().strftime('%H:%M:%S')} : Tweeting: {text} + Image: {imageurl}")
    os.remove(mediapath)

#tweet from the que.txt file
def tweetfromque():
    global firstline, secondline, tweetimageurl, tweetmessage

    try:
        #open que.txt
        file = open("que.txt")

        #set strigns to None to start with
        tweetimageurl = None
        tweetmessage = None

        file.seek(0) #go to the beginning of the que file
        firstline = file.readline() #save the first line as firstline


        if firstline.startswith("{image}"): #if {image} tag in line then remove it and save remaining url
            firstline = firstline.replace('{image}', '')
            tweetimageurl = firstline
            secondline = file.readline()
            tweetmessage = secondline

            #delete used lines:
            lines = []# list to store file lines

            with open(r"que.txt", 'w+') as fp:
                lines = fp.readlines()# read and store all lines into list
                
                for number, line in enumerate(lines):# wipe lines 1 & 2 (0,1)
                    if number not in [0, 1]:
                        fp.write(line)
                fp.close() #close file

        else: #if no {image} tag at beginning of the line, save as just tweetmessage
            tweetmessage = firstline

        if tweetmessage == None or tweetmessage == '':
            print(f"{datetime.now().strftime('%H:%M:%S')} Unable To Post From The Que, Today You Get This Message As A Tweet")
            tweet(f"Unable To Post From The Que, Today({datetime.now().strftime('%D @ %H:%M:%S')}) You Get This Message As A Tweet")
            
        else: #if tweetmessage exists
            if tweetimageurl != None: #if imageurl provided (if posting image) then do so
                print(f"{datetime.now().strftime('%H:%M:%S')} Tweeted Image : {tweetimageurl} + Caption : {tweetmessage}")
                tweetimagewithurl(tweetimageurl,tweetmessage)
                
            elif tweetimageurl == None:#if imageurl not provided (if not posting image) then do so
                print(f"{datetime.now().strftime('%H:%M:%S')} Tweeted Message : {tweetmessage}")
                tweet(tweetmessage)



        file.close()#close file

    except:
        print(f"{datetime.now().strftime('%H:%M:%S')} [Caught the exception - line 120 functions.py] Unable To Post From The Que, Today You Get This Message As A Tweet")
        tweet(f"Unable To Post From The Que, Today({datetime.now().strftime('%D @ %H:%M:%S')}) You Get This Message As A Tweet")

#dm someone text-only
def directmessage(user, text):
    api.send_direct_message(recipientid(user), text)

#dm someone attachment
def directmessageattachment(user,text,url):
    mediapath = './images'
    myfile = requests.get(url)
    open(mediapath, 'wb').write(myfile.content)
    uploadedmedia = api.media_upload(filename=mediapath)
    api.send_direct_message(recipientid(user), text, attachment_type='media', attachment_media_id = uploadedmedia.media_id)
    os.remove(mediapath)

#gets a certain users info
def userinfo(username):
    #The snippet below fetches a user, and then prints its details as well as its 20 most recent followers:
    user = api.get_user(screen_name=username)

    print("User details:")
    print(user.name)
    print(user.description)
    print(user.location)
    print("")
    print("Last 20 Followers:")
    for follower in user.followers():
        print(follower.name)

#follow a certain user
def follow(user):
    # This code shows how you can use Tweepy to start following a user:
    api.create_friendship(user)

#update profile description
def updatedescription(text):
    # You can use this code snippet to update your profile description:
    api.update_profile(description=text)

#like the most recent tweet in your timeline
def likerecenttweet():
    # You can mark the most recent tweet in your home timeline as Liked as follows:
    tweets = api.home_timeline(count=1)
    tweet = tweets[0]
    print(f"Liking tweet {tweet.id} of {tweet.author.name}")
    api.create_favorite(tweet.id)

#list all blocked users
def listblockedusers():
    # Here’s how you can see the users that you have blocked:
    for block in api.blocks():
        print(block.name)

# get followers of a certain user (return only)
def getfollowers(username):
    # this wil get the followers of the specified user
    user = api.get_user(screen_name=username)
    listofusernames = None
    for follower in user.followers():
        listofusernames = f"{listofusernames}, {follower.screen_name}"
        listofusernames = listofusernames.replace('None, ', '')
    return listofusernames

# get followers of a certain user (printout)
def listfollowers(username):
    # this wil get the followers of the specified user
    user = api.get_user(screen_name=username)
    listofusernames = None
    for follower in user.followers():
        print("Name: "+ follower.name)
        print("Username: " + follower.screen_name)
        print("")
        listofusernames = f"{listofusernames}, {follower.screen_name}"
        listofusernames = listofusernames.replace('None, ', '')
    return listofusernames

#check for new followers & new unfollowers
def checknewfollowers():
    global previous_followers_list
    global unfollowers_list
    unfollowers_list = [] #wipe unfollowers list    

    #get current follower list - save as changing variable new_followers_list
    new_followers_list = getfollowers(me) #save the second set of followers in a list
    copy_new_followers_list = new_followers_list #duplicate new_followers_list
    copy_new_followers_list = list(copy_new_followers_list.split(", ")) #convert string to list
    new_followers_list = list(new_followers_list.split(", ")) #convert string to list

    for user in previous_followers_list: #for each user in previous list remove them from new list, if it doesnt work then they have unfollowed
        try:
            new_followers_list.remove(user)
        except:
            unfolloweduser = f"{user}"
            unfollowers_list.append(unfolloweduser)


    print()
    if unfollowers_list == None or unfollowers_list == 'None':
        unfollowers_list == []

    '''if unfollowers_list == [] and new_followers_list == []:
        print(f"{datetime.now().strftime('%H:%M:%S')} - Account Stayed The Same.")'''
    
    if unfollowers_list != []:
        for user in unfollowers_list:
            print(f"{datetime.now().strftime('%H:%M:%S')} - {user} unfollowed you :(")
            tweet(f"So Sorry To see You Go @{user} :( 👋")
    if new_followers_list != []:
        for user in new_followers_list:
            print(f"{datetime.now().strftime('%H:%M:%S')} - {user} followed you :))")
            tweet(f"Yay, Welcome To The Gang @{user} 👋,\n To See My Work Visit https://github.com/CryptoidCoder/")


    previous_followers_list = copy_new_followers_list #set previous as the current for next time
    
#fetch last 10 tweets with certain text in them
def search(text):
    # For example, you can try this code to get the 10 most recent public tweets that are in English and contain a certain word:
    for tweet in api.search(q=text, lang="en", rpp=10):
        print(f"{tweet.user.name}:{tweet.text}")

#fetch trending tweets
def listtrending():
    # For example, here’s how to list the world-wide trending topics:
    trends_result = api.trends_place(1)
    for trend in trends_result[0]["trends"]:
        print(trend["name"])

#fetch tweets your mentioned in
def mentioned():
    # Fetch every tweet in which you are mentioned, and then mark each tweet as Liked and follow its author. You can do that like this:
    tweets = api.mentions_timeline()
    for tweet in tweets:
        tweet.favorite()
        tweet.user.follow()

#fetch x items from your timeline
def fetchitems(number):
    # This code shows how, by using a cursor, you can get not only the first page from your timeline, but also the last however many tweets:
    for tweet in tweepy.Cursor(api.home_timeline).items(number):
        print(f"{tweet.user.name} said: {tweet.text}")


#Definitions@
#get current follower list - save as static variable original_followers_list
original_followers_list = getfollowers(me) #save the first set of followers in a list

#duplicate into a changing variable - previous_followers_list
previous_followers_list = original_followers_list
previous_followers_list = list(previous_followers_list.split(", ")) #convert string to list