# TwitterBot (cloudrun version)

This projects is so that I can use the Twitter API

Currently it will be used for messaging new followers & posting daily.
- Hosted on [pythonanywhere](https://www.pythonanywhere.com)

### Files:
- `authenticationtest.py` {This will make sure your api keys are working and the .env is formatted correctly.}
- `functions.py` {This is where all of my functions are, tweet() etc.}
- `main.py` {this will schedule tasks to happen (tweets / new follower checks)}

### Format of the `.env`:
```
#API keys:
API_key = "xxxxxxxxxxxxxxxxxxxxxxxxx"
API_key_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

Access_token = "xxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
Access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

my_username = 'xxxxx'

```

### Format of the `que.txt`:
tweet & image:
- {image}https://web-location-of-image-you-want-to-tweet.com/image.png
- Text to tweet alongside the image here

text-only tweet:
- Text to tweet here
```
{image}https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.ubux1yLT726_fVc3A7WSXgHaHa%26pid%3DApi&f=1
This is an automated tweet using tweepy that takes a url and text and automatically downloads & tweets it.
Today it'll just be a tweet

```

You will need to create the twitter developer application and give it `Read, Write, Direct Message` permissions.

[Here is a link to help you do that.](https://blog.hubspot.com/website/how-to-make-a-twitter-bot)


