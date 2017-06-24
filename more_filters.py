# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 19:09:52 2017

@author: chetan
"""

# Count terms only once, equivalent to Document Frequency
terms_single = set(terms_all)
# Count hashtags only
terms_hash = [term for term in preprocess(tweet['text']) 
              if term.startswith('#')]
# Count terms only (no hashtags, no mentions)
terms_only = [term for term in preprocess(tweet['text']) 
              if term not in stop and
              not term.startswith(('#', '@'))] 
              # mind the ((double brackets))
              # startswith() takes a tuple (not a list) if 
              # we pass a list of inputs
              
              
from nltk import bigrams 
 
terms_bigram = bigrams(terms_stop)