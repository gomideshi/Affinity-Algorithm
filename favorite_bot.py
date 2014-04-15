import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time, random

OAUTH_TOKEN = '-REMOVED-'
OAUTH_SECRET = '-REMOVED-'
CONSUMER_KEY = '-REMOVED-'
CONSUMER_SECRET = '-REMOVED-'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
api = tweepy.API(auth)

print '*********************'
print 'AUTH @'+ api.me().screen_name
print '*********************'

class listener(StreamListener):
    def on_data(self, data):
        try:
            #ROLLING FREEZE DICE#
            Action = random.randint(1,3)
            P1 = random.randint(40,60)
            P2 = random.randint(50,70)

            #DATA SEGMENTATION#
            theID = data.split(',"id":')[1].split(',"id_str":"')[0]
            tweet = data.split(',"text":"')[1].split('","source')[0]
            username = data.split(',"screen_name":"')[1].split('","location')[0]

            #CLIENT PRINT OUTPUT#
            print 'U/N: ' + username
            print 'TWEET: ' + tweet
            print 'TWEET ID: ' + theID + ' +FAV' + '\n'

            #PAUSE[1], ACTION DICE, PAUSE[2]#
            time.sleep(P1)

            if Action==1:
                api.create_friendship(username)

            if Action==2:
                api.retweet(theID)

            if Action==3:
                api.create_favorite(theID)
                
            time.sleep(P2) 

            return True
        except BaseException, e:
            
            print 'failed ondata,',str(e)
            time.sleep(5)

    def on_error(self, status):
        print status

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["banksy"])
