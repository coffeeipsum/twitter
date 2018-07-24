# in a real life scenario you would add this py file to .gitignore (to keep the API keys hidden)

import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = '8l2AuJLFehoqbikiPhHhfJpj8'
CONSUMER_SECRET = 'HCG2Z6IdzrWms2R5VCTNaAGRTT0i51MTkzPPvQmRTg3dSWfL0S'
OAUTH_TOKEN = '761230413209669636-tw2I4YVKRpPy6zWwSnQPiXlYhwOgpaE'
OAUTH_TOKEN_SECRET = '4k0iTtNQQrHqkaMd8T33Jxre2gcx1D2SnWK7laUfZQrnY'

def get_auth():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return auth
    
def twitter_api():
    auth = get_auth()
    return tweepy.API(auth)