import tweepy
import yaml

def setupTwitterAutorization(envconfig) :
    with open(envconfig, 'r') as f:
        doc = yaml.load(f)

    api_key = doc['twitter']['api_key']
    api_secret = doc['twitter']['api_secret']
    access_token = doc['twitter']['access_token']
    access_token_secret = doc['twitter']['access_token_secret']
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api
