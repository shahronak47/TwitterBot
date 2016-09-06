library(twitteR)
api_key <- "cgn3knVWtwlPBmnkAwcdixUyR"
api_secret <- "chzW3apv7Km5qin8C9rlJC7LywBhTBNHolIO4ITbKJp4csumRK"
access_token <- "4689595801-XFdnbJlga3AOxo9yhv6e5tfU6oY19fDaAvc6aDn"
access_token_secret <- "nceL2eTEtiJzcPz5jK6j4ItDHDQAL9P9UHcnwVfATDaEK"
options(httr_oauth_cache=T)
setup_twitter_oauth(api_key,api_secret,access_token,access_token_secret)
searchResult <- searchTwitter('#GoodMorning', n=1, lang = 'en')
tweetDetailsDF <- twListToDF(searchResult)
updateStatus(paste(paste0("@", tweetDetailsDF$screenName), "Good Morning, Have a nice day! :) "), inReplyTo = tweetDetailsDF$id)
  