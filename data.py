# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 11:58:21 2017

@author: chetan
"""

import tweepy
from tweepy import OAuthHandler
import json
# palce your keys in the below fields to acces data. 
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

for tweet in tweepy.Cursor(api.user_timeline).items():
    print(tweet.text)
