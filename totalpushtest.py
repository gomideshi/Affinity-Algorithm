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

gate = 'NOPASS'
again = 'y'
while again=='y':
    
    qbdir = open("quotebank.txt", "r")
    data = qbdir.readlines()

    while gate == 'NOPASS':
        X=random.randint(1,10)
        if str(X) in open('CHECKPOINT.txt').read():
            gate = 'NOPASS'
        else:
            gate = 'PASS'

    checkpoint = open("CHECKPOINT.txt", "a")    
    checkpoint.write(str(X)+'\n')   
    quotedrop = data[X].strip()
    
    api.update_with_media('C:/Users/Administrator/Documents/w5748/robotarmy/img/'+str(X)+'.png', quotedrop)

    qbdir.close()
    checkpoint.close() 

    again = raw_input('again? y/n')
    gate = 'notcool'

