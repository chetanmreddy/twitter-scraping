# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 11:58:21 2017

@author: chetan
"""

import tweepy
from tweepy import OAuthHandler
import json
 
consumer_key = 'tXDMxiycRFMEqZUMgF8eiOnKi'
consumer_secret = 'HFqfmJeErViUQGYEcpH2mXbSnzN1NLKtSaRW0mHind9V0CBvg3'
access_token = '2229878924-F6wIrxf0U86O6icfXyrDyX4NYAkqAH2oBKg7fUr'
access_secret = 'f1HrOIUk2X1q7LmVXHnyksnfeL0iLEDJUj1vudqKJYED4'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

for tweet in tweepy.Cursor(api.user_timeline).items():
    print(tweet.text)