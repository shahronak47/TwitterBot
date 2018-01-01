import pdb
from setupTwitterAuthorization import setupTwitterAutorization

if __name__ == "__main__":
    api = setupTwitterAutorization('C:\\Users\\Ronak Shah\\Google Drive\\TwitterBot\\rstats\\keys.yml')
    # Search for #rstats
    searchResult = api.search('#rstats -filter:retweets')

    for result in searchResult :

        if not result.retweeted :
            try :
                api.retweet(result.id)

            except Exception as error:
               continue
