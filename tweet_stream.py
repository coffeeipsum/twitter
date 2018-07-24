import json
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from twitter_hidingKeys import get_auth, twitter_api

api = twitter_api


CONSUMER_KEY = '8l2AuJLFehoqbikiPhHhfJpj8'
CONSUMER_SECRET = 'HCG2Z6IdzrWms2R5VCTNaAGRTT0i51MTkzPPvQmRTg3dSWfL0S'
OAUTH_TOKEN = '761230413209669636-tw2I4YVKRpPy6zWwSnQPiXlYhwOgpaE'
OAUTH_TOKEN_SECRET = '4k0iTtNQQrHqkaMd8T33Jxre2gcx1D2SnWK7laUfZQrnY'


keyword_list = ["python," "javascrip", "php", "C#"]  # to track list

limit = 500

class MyStreamListener(StreamListener):
    
    def __init__(self):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        
    def on_data(self, data):
        if self.num_tweets < limit:
            self.num_tweets += 1
            try:
                with open('tweet_mining.json', 'a') as tweet_file:
                    tweet_file.write(data)
                    return True
            except BaseException as e:
                print("Failed on_data: %s"%str(e))
            return True
        else:
            return False
        
        
    def on_error(self, status):
        print(status)
        return True
        
        
auth = get_auth()

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)