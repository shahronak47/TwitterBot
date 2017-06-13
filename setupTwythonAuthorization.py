from twython import Twython

def twython_authorization () :
    api_key = "api_key"
    api_secret = "api_secret"
    access_token = "access_token"
    access_token_secret = "access_token_secret"
    twythonObject = Twython(api_key, api_secret, access_token,access_token_secret)
    return  twythonObject
