
#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
from tweepy import OAuthHandler
import json
import wget

#Twitter Authentication
with open('twitter_credentials.json') as cred_data:
info = json.load(cred_data)
consumer_key = info['CONSUMER_KEY']
consumer_secret = info['CONSUMER_SECRET']
access_token = info['ACCESS_KEY']
access_secret = info['ACCESS_SECRET']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#Creating tweepy api
api = tweepy.API(auth)

user = \
input("Enter twitter user_id - "
)

#Getting all tweets
all_tweets = api.user_timeline(screen_name=user, count=200,
include_rts=False, exclude_replies=True)

last_tweet_id = all_tweets[-1].id

#Getting more tweets
while True:
more_tweets = api.user_timeline(screen_name=user, count=200,
include_rts=False,
exclude_replies=True,
max_id=last_tweet_id - 1)

if len(more_tweets) == 0:
break
else:
last_tweet_id = more_tweets[-1].id - 1
all_tweets = all_tweets + more_tweets

image_files = set()
for status in all_tweets:
media = status.entities.get('media', [])
if len(media) &amp;amp;amp;amp;gt; 0:
image_files.add(media[0]['media_url'])

print ('Downloading ' + str(len(image_files)) + ' images.....')
for image_file in image_files:
wget.download(image_file)
Once you run it, you will be asked for the twitter id whose images you want to download. On entering the id, the program will run for some time and then start downloading the images one by one.

Since the folder in which you run this program will be filled with hundreds of images, I recommend that you run this program in a separate folder so that you do not need to separate images from other files.

Extracting tweets containing a particular hashtag from twitter:
The code given next, can be used to extract n number of tweets with a given hashtag into a text file. Both the number of tweets and the hashtag itself are user inputs and the scraping will happen only when you have provided both the inputs. I must mention again that you need to have the twitter_credentials.json in the same folder as this file, to make sure that the program runs.
