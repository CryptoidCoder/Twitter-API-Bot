import tweepy
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_key = os.getenv("API_key")
API_key_secret = os.getenv("API_key_secret")
Access_token = os.getenv("Access_token")
Access_token_secret = os.getenv("Access_token_secret")

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_key,API_key_secret)
auth.set_access_token(Access_token,Access_token_secret)




# Create API object
#api = tweepy.API(auth, wait_on_rate_limit=True,
#    wait_on_rate_limit_notify=True)

api = tweepy.API(auth)

me = tweepy.API.verify_credentials()

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

#tweet a text-only message
def tweet(text):
    # The following code uses Tweepy to create a tweet with some text:
    api.update_status(text)

#tweets message with image
def tweetimage(pathtoimage, text):
    api.update_with_media(pathtoimage,text)

#dm someone text-only
def directmessage(user, text):
    api.send_direct_message(recipientid(user), text)

#dm someone attachment
def directmessageattachment(user,text,url):
    mediapath = '/home/CryptoidCoder/tweepy-bots/images/media'
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

# list followers of a certain user
def getfollowers(username):
    # this wil get the followers of the specified user
    user = api.get_user(screen_name=username)
    for follower in user.followers():
        print("Name: "+ follower.name)
        print("Username: " + follower.screen_name)
        print("")

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