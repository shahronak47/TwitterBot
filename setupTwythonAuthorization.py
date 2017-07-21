from twython import Twython
import yaml

def twython_authorization () :
    envconfig = 'F:\My Stuff\Python Twitter Project\keys.yml'
    with open(envconfig, 'r') as f:
        doc = yaml.load(f)

    api_key = doc['twitter']['api_key']
    api_secret = doc['twitter']['api_secret']
    access_token = doc['twitter']['access_token']
    access_token_secret = doc['twitter']['access_token_secret']

    twythonObject = Twython(api_key, api_secret, access_token,access_token_secret)
    return  twythonObject
