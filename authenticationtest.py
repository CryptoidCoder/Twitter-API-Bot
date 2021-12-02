import tweepy
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

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
    print(api.verify_credentials().screen_name)
except:
    print("Error during authentication")