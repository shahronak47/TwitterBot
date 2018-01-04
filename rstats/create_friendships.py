from setupTwythonAuthorization import twython_authorization

def create_frienships (followIds) :
    api = twython_authorization('C:\\Users\\Ronak Shah\\Google Drive\\TwitterBot\\rstats\\keys.yml')
    for id in followIds :
    #Follow the specified user

        try:
            api.create_friendship(user_id = id)
    #Mute the specified user
            api.create_mute(user_id= id)
        except:
            pass






