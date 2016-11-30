import sys
import tweepy

api_key = "api_key"
api_secret  = "api_secret"
access_token = "access_token"
access_token_secret = "access_token_secret"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api.create_friendship(sys.argv[1])