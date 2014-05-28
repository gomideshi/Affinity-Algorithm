import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time, random

OAUTH_TOKEN = '2444919187-2iQehpSc7JaER4TaHDNuWKECcCgUjBzmG9bMK5Q'
OAUTH_SECRET = '3h1O4YGMznzufZoJsc2KctG4mzXix1ec5GY3HN3HG8gUu'
CONSUMER_KEY = 'Ee5M6ruuchxDMt7nRObs0UYEB'
CONSUMER_SECRET = 'DwNSMTKN0lOqWLC5xbTawzfiF5PIrdIYO7w7OXfWWG50H4VdFm'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
api = tweepy.API(auth)

print '*********************'
print 'AUTH @'+ api.me().screen_name
print '*********************'


x = random.randint(1,10)
api.update_with_media('C:/Users/Administrator/Documents/w5748/robotarmy/img/'+str(x)+'.png', 'test')
