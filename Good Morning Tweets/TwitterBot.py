from setupTwitterAuthorization import setupTwitterAutorization
from create_friendships import create_frienships
from destroy_friendships import destroyFriendships
import pdb

if __name__ == "__main__":

    #Setting up twitter authorization
    api = setupTwitterAutorization('keys.yml')
    try: 
    #Search for #GoodMorning
        searchResult = api.search('#GoodMorning -filter:retweets', count = 1)
        #Take only first tweet
        if not not searchResult:
            tweet = searchResult[0]
            if not tweet.retweeted :
                api.update_status("@" + tweet.user.screen_name + " Good Morning, Have a nice day! :-) ", tweet.id)

    except Exception as error :
        #Handle duplicate status exception
            if error[0][0]['code'] == 187 :
                tweet = searchResult[1]
                api.update_status("@" + tweet.user.screen_name + " Good Morning, Have a nice day! :-) ", tweet.id)
        #Get the followers
        followerIds = api.followers_ids()
        friendIds = api.friends_ids()
        #Get people to follow
        followIds = list(set(followerIds) - set(friendIds))
        #Get people to unfollow
        unfollowIds = list(set(friendIds) - set(followerIds))

        if not not followIds :
            create_frienships(followIds)

        if not not unfollowIds :
            destroyFriendships(unfollowIds)
