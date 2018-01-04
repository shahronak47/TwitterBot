from twython import Twython
import yaml

def twython_authorization (envconfig) :
    with open(envconfig, 'r') as f:
        doc = yaml.load(f)

    api_key = doc['api_key']
    api_secret = doc['api_secret']
    access_token = doc['access_token']
    access_token_secret = doc['access_token_secret']

    twythonObject = Twython(api_key, api_secret, access_token,access_token_secret)
    return  twythonObject
