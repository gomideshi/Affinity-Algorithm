import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time, random

OAUTH_TOKEN = '###'
OAUTH_SECRET = '###'
CONSUMER_KEY = '###'
CONSUMER_SECRET = '###'

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
            ActionCalc = random.randint(1,95)
            Action = 0
            if ActionCalc <= 59:
                Action = 1
            if ActionCalc >= 60 and ActionCalc <= 74:
                Action = 2
            if ActionCalc >= 75 and ActionCalc <= 90:
                Action = 3
            if ActionCalc >= 91 and ActionCalc <= 95:
                Action = 4

            #PAUSE DICE#
            P1 = random.randint(90,300)

            #DATA SEGMENTATION#
            tweetID = data.split(',"id":')[1].split(',"id_str":"')[0]
            tweet = data.split(',"text":"')[1].split('","source')[0]
            username = data.split(',"screen_name":"')[1].split('","location')[0]

            #OUTPUT FROM API#
            print 'USER: ' + username
            print 'TWEET: ' + tweet
            print 'TWEET ID: ' + tweetID
            print 'ROLL: '+str(ActionCalc)+'/95 - OPERATION #'+str(Action)

            #PASS RETWEETS#
            if 'RT ' in tweet:
                Action = 0
                print 'RETWEET! ** AUTOMATIC MUULIGAN**'
                time.sleep(2)

            #ACTION FORK#
            if Action == 1:
                print 'ACTION: **MULLIGAN**'
                time.sleep(2)
                
            if Action == 2:
                print 'ACTION: *FOLLOWING* IN ' + str(P1) + ' SECONDS.'
                time.sleep(P1)
                api.create_friendship(username)

            if Action == 3:
                print 'ACTION: *FAVORITING* IN ' + str(P1) + ' SECONDS.'
                time.sleep(P1)
                api.create_favorite(tweetID)

            if Action == 4 and 't.co' in tweet:
                print 'ACTION: *RETWEETING* IN ' + str(P1) + ' SECONDS.'
                time.sleep(P1)
                api.retweet(tweetID)
                

            #ACTION COMPLETE - CYCLE END#
            print '------------------------------------------'
            print '[COMPLETE] NEXT CYCLE BEGINS IN 3 SECONDS.' + '\n'
            time.sleep(3)

            return True
        except BaseException, e:
            
            print 'ERROR: '+str(e)+'\n'
            time.sleep(5)

    def on_error(self, status):
        print status

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["banksy", "graffiti"])
