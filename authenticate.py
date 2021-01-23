import tweepy
import os
from functions import *

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")