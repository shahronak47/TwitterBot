import tweepy
import yaml

def setupTwitterAutorization(envconfig) :
    with open(envconfig, 'r') as f:
        doc = yaml.load(f)

    api_key = doc['api_key']
    api_secret = doc['api_secret']
    access_token = doc['access_token']
    access_token_secret = doc['access_token_secret']
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api
