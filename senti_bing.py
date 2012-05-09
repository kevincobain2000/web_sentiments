#! /usr/bin/env python
# -*- coding: utf-8 -*-
import warnings
from pybing import Bing
import nltk
from urllib import urlopen
from senti_classifier import senti_classifier
try: bing = Bing()
except: bing = Bing('<your AppId here>')

def search(query, fetch = None):
    #fetch: [u'Url', u'DateTime', u'DisplayUrl', u'Description', u'Title']
    response = bing.search_web(query)
    results = response['SearchResponse']['Web']['Results']
    if not fetch: return results
    else: return [r[fetch] for r in results]
def dehtml(url):
    html  = urlopen(url).read()
    raw = nltk.clean_html(html)
    return raw

def raw_outs(query):
    #reads urls and returns raw text if line in rawtext contains the query term
    urls = search(query, 'Url')
    raw = []
    for url in urls:
        try:
            for line in dehtml(url).splitlines():
                if query.lower() in ' '.join([w.lower() for w in line.split()]):
                    raw.append(line)
        except: pass
    return set(raw)
    
if __name__ == '__main__':
    query = 'earthquake'
    lines = raw_outs(query)
    print senti_classifier.polarity_scores(lines)
    
    
    
    
    
    
    
        

