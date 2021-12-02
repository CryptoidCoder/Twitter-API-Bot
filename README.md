# TwitterBot (cloudrun version)

This projects is so that I can use the Twitter API

Currently it will be used for messaging new followers & posting daily.
- Hosted on [pythonanywhere](https://www.pythonanywhere.com)

### Files:
- `authenticationtest.py` {This iwll make sure your api keys are working and the .env is formatted correctly.}
- `functions.py` {This is where all of my functions are, tweet() etc.}
- `main.py` {this will schedule tasks tohappen (tweets / new follower checks)}

### Format of the `.env`:
```
#API keys:
API_key = "xxxxxxxxxxxxxxxxxxxxxxxxx"
API_key_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

Access_token = "xxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
Access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

```

You will need to create the app and give it `Read, Write, Direct Message` permissions.

[Here is a link to help you do that.](https://blog.hubspot.com/website/how-to-make-a-twitter-bot)


