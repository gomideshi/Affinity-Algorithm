import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time, random
from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
api = tweepy.API(auth)

print '*********************'
print 'AUTH @'+ api.me().screen_name
print '*********************'

class listener(StreamListener):
    def on_data(self, data):
        try:
            #CYCLE START - ACTION DICE#
            ActionCalc = random.randint(1,1000)
            ActionGate = random.randint(1,5)
            Action = 0
            
            if ActionCalc <= 990 or ActionCalc == 1000: #Pass 99.9%
                Action = 1
            if ActionCalc >= 991 and ActionCalc <= 994: # follow
                if ActionGate == 1:
                    Action = 2
                else:
                    Action = 0
            if ActionCalc >= 995 and ActionCalc <= 998: #4% favorite
                if ActionGate == 1:
                    Action = 3
                else:
                    Action = 0
            if ActionCalc == 999: #1% retweet
                if ActionGate == 1:
                    Action = 4
                else:
                    Action = 0

            #DATA SEGMENTATION#
            tweetID = data.split(',"id":')[1].split(',"id_str":"')[0]
            tweet = data.split(',"text":"')[1].split('","source')[0]
            username = data.split(',"screen_name":"')[1].split('","location')[0]

            #OUTPUT FROM API#
            print 'USER: ' + username
            print 'TWEET: ' + tweet

            #PASS RETWEETS#
            if 'RT ' in tweet:
                Action = 0
                print 'RETWEET! ** AUTOMATIC MUULIGAN**'

            #ACTION FORK#
            if Action == 1:
                print 'ACTION: **MULLIGAN**'
                
            if Action == 2:
                print 'ACTION: *FOLLOWING*!'
                api.create_friendship(username)
                time.sleep(4)

            if Action == 3:
                print 'ACTION: *FAVORITING*!'
                api.create_favorite(tweetID)
                time.sleep(4)

            if Action == 4 and 't.co' in tweet:
                print 'ACTION: *RETWEETING*!'
                api.retweet(tweetID)
                time.sleep(4)

            print ''

            return True
        except BaseException, e:
            
            print 'ERROR: '+str(e)+'\n'
            time.sleep(5)

    def on_error(self, status):
        print status

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["banksy", "graffiti", "art", "music"])
