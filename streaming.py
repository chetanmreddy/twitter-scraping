# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 12:24:38 2017

@author: chetan
"""

from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json
import tweepy
import config
 

auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
api = tweepy.API(auth)
    
    
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('frenchopen.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print('error')
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['frenchopen'])