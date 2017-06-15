from setupTwythonAuthorization import twython_authorization

def create_frienships (followIds) :
    api = twython_authorization()
    for id in followIds :
    #Follow the specified user
        api.create_friendship(user_id = id)
    #Mute the specified user
        api.create_mute(user_id= id)





