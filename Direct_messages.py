import tweepy
import pandas as pd
import yaml
import random


def setupTwitterAutorization() :

    envconfig = 'F:\My Stuff\Python Twitter Project\keys.yml'
    with open(envconfig, 'r') as f:
        doc = yaml.load(f)

    api_key = doc['twitter']['api_key']
    api_secret = doc['twitter']['api_secret']
    access_token = doc['twitter']['access_token']
    access_token_secret = doc['twitter']['access_token_secret']

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

#Extract Direct messages which are recieved and sent

def GetDirectMessagesInOrder () :

    receivedMsgs = api.direct_messages(count = 200)
    sentMsgs = api.sent_direct_messages(count = 200)

    #Now extract the convesation only between the two users which we are interested in
    receiveText = []; recieveTime = []; tweetId = [];


    for eachRDM in receivedMsgs :

        receiveText.append(eachRDM.text)
        recieveTime.append(eachRDM.created_at)
        tweetId.append(eachRDM.id)

    for eachSDM in sentMsgs :
        receiveText.append(eachSDM.text)
        recieveTime.append(eachSDM.created_at)
        tweetId.append(eachSDM.id)
    #Combine two arrays of sent and recieved

    abc = pd.DataFrame({'Tweet Id' : tweetId,'Timestamp' : recieveTime, 'Text' : receiveText, 'Said By' : saidBy})
    #Sort by timestamp so you could get an exact conversation
    if(abc.shape[0] > 0) :
        abc.sort_values('Timestamp', inplace = True)
        abc.to_csv("F:\\temp" + str(random.randint(1, 10000)) + ".csv", encoding='utf-8')

    return abc

def DeleteRetrievedMessages(tweetIDs) :
    try :
        for id in tweetIDs :
            api.destroy_direct_message(id)
    except :
        pass

if __name__ == "__main__":
    completeList = []
    dataLeft = True
    #Setting up twitter authorization
    api = setupTwitterAutorization()
    while(dataLeft) :

        # Get one batch of msgs
        newDF = GetDirectMessagesInOrder()
        #pdb.set_trace()
        if (newDF.shape[0] > 0):
            completeList.append(newDF)
            # Delete those msgs
            DeleteRetrievedMessages(newDF['Tweet Id'])

    df = pd.concat(completeList)
    df.sort_values('Timestamp', inplace=True)
    df.to_csv("F:\Final.csv", encoding='utf-8')


