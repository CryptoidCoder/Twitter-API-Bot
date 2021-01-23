# TwitterBot

This projects is so that I can use the Twitter API

Currently it will be used for messaging new followers.

### Files:
- `authenticate.py` {This iwll make sure your api keys are working and the .env is formatted correctly.}
- `follow_followers.py` {This will  check for new followers evry minute and if they are new, then it will tweet saying hello.}
- `functions.py` {This is where all of my functions are, tweet() etc.}
- `streams.py` {This will look for tweets with certian words in, and then it will like and retweet them. - be warned this will not be able to run for long as the twitter APi has a requests cap.}

### Format of the `.env`:
```
#API keys:
API_key = "xxxxxxxxxxxxxxxxxxxxxxxxx"
API_key_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

Access_token = "xxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
Access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

thingstolookfor = "'@thing','#thing', 'thing'"

```

You will need to create the app and give it `Read, Write, Direct Message` permissions.

[Here is a link to help you do that.](https://blog.hubspot.com/website/how-to-make-a-twitter-bot)


## TODO:
### `follow_followers.py`:
- Change it so that it stores the followers in a .txt rather than a list- so that you don't have to have it always running. and it will still work.
- I also need to find a way for it check if anyone unfollowed.

