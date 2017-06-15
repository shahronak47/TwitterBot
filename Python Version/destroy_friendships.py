from setupTwythonAuthorization import twython_authorization

def destroyFriendships(unfollowIds) :
    api = twython_authorization()
    for id in unfollowIds :
        api.destroy_friendship(user_id = id)

