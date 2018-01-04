from setupTwitterAuthorization import setupTwitterAutorization
from create_friendships import create_frienships
from destroy_friendships import destroyFriendships

if __name__ == "__main__":
    api = setupTwitterAutorization('C:\\Users\\Ronak Shah\\Google Drive\\TwitterBot\\rstats\\keys.yml')
    # Search for #rstats
    searchResult = api.search('#rstats')

    for result in searchResult :
        if not result.retweeted :
            try :
                api.retweet(result.id)

            except Exception as error:
               continue

    # Get the followers
    followerIds = api.followers_ids()
    friendIds = api.friends_ids()
    # Get people to follow
    followIds = list(set(followerIds) - set(friendIds))
    # Get people to unfollow
    unfollowIds = list(set(friendIds) - set(followerIds))

    if not not followIds:
        create_frienships(followIds)

    if not not unfollowIds:
        destroyFriendships(unfollowIds)

