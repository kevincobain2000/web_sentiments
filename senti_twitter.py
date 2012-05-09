#! /usr/bin/env python
# -*- coding: utf-8 -*-
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    import twitter
from senti_classifier import senti_classifier
api_keys = {'consumer_key' : '',
            'consumer_secret' : '',
            'access_token_key' : '',
            'access_token_secret' : ''}
def get_api_keys(api_keys):
    #return {'consumer_secret': 'a4ksdf7s, 'consumer'....
    if len([key for key in api_keys.values() if key]) <4:
        keys = open('_twitter.api','r').readlines()
        for line in keys:
            key,val  = [k.strip() for k in line.split('\t') if k]
            api_keys[key] = val
    return api_keys

def twitter_api():
    _api_keys = get_api_keys(api_keys)
    api = twitter.Api()
    api = twitter.Api(consumer_key = _api_keys['consumer_key'],
                      consumer_secret = _api_keys['consumer_secret'],
                      access_token_key = _api_keys['access_token_key'],
                      access_token_secret = _api_keys['access_token_secret'])
    return api
def tweets(usr=None):
    api = twitter_api()
    statuses = api.GetUserTimeline("TheSJFC")
    _tweets = [s.text for s in statuses]
    return _tweets
    
if __name__ == '__main__':
    pos, neg = senti_classifier.polarity_scores(tweets(usr = "TheSJFC"))
    print pos, neg
    
    
        

