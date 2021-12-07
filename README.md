# TwitterBot (cloudrun version)

This projects is so that I can use the Twitter API

Currently it will be used for messaging new followers & posting daily.
- Hosted on [heroku](https://www.heroku.com)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## To Run:
1) Deploy to heroku (use the button above / clone the repo and deploy your own way).
2) Fill in environment variables with appropriate details (API & Access keys, twitter username) [Link On How-To Here](https://catalins.tech/heroku-environment-variables).
4) Make sure the `worker: python main.py` & `web: python server.py` is turned on on the app dashboard.

### Files:
- `functions.py` {This is where all of my functions are, tweet() etc}.
- `main.py` {This will schedule tasks to happen (tweets / new follower checks)}.
- `server.py` {This will run a `Hello World server for heroku`}.

### Format of the `Environment Variables`:
```
Key:API_key, Value:"xxxxxxxxxxxxxxxxxxxxxxxxx"
Key:API_key_secret, Value:"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

Key:Access_token, Value:"xxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
Key:Access_token_secret, Value:"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

Key:my_username, Value:'xxxxx'

```

<!--
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
-->

You will need to create the twitter developer application and give it `Read, Write, Direct Message` permissions.

[Here is a link to help you do that.](https://blog.hubspot.com/website/how-to-make-a-twitter-bot)


