import urllib
import urllib2
import simplejson as json
import re

SEARCH_BASE = 'http://otter.topsy.com/search.json'
APP_ID = 'BB4FC86DF8674F76838FB55EED311689'

class Tweet:
    hits = 0
    author = ''
    content = ''
    def printTweet(self):
        print ('Hits: ' + str(self.hits) + ' Author: ' + self.author + '\nTweet: ' + self.content + '\n')
        
def search(query, results=20, start=1, **kwargs):
    kwargs.update({
        'apikey': APP_ID,
        'q': query,
        'results': results,
        'start': start
    })
    URL = SEARCH_BASE + '?' + urllib.urlencode(kwargs)
    print URL
    
    result = json.load(urllib.urlopen(URL))
    if 'Error' in result:
        # An error occurred; raise an exception
        print 'Error in json request'
        # raise YahooSearchError, result['Error']
    return result['response']['list']
   
""" entry point """ 

candidates = ['Mitt Romney', 'Rick Santorum', 'Newt Gingrich']
    
for candidate in candidates:
    info = search(candidate)
    #Tweets is a list of dictionaries, where each dictionary is a tweet. The keys are the different parts of the tweet
    tweetList = []
    for tweet in info:
        t = Tweet() 
        t.hits = tweet['hits']
        t.author = tweet['trackback_author_nick']
        t.content = tweet['content']
        t.printTweet()
    