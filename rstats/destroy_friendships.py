from setupTwythonAuthorization import twython_authorization

def destroyFriendships(unfollowIds) :
    api = twython_authorization('C:\\Users\\Ronak Shah\\Google Drive\\TwitterBot\\rstats\\keys.yml')
    for id in unfollowIds :
        api.destroy_friendship(user_id = id)

