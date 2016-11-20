library(twitteR)
api_key <- "api_key"
api_secret <- "api_secret"
access_token <- "access_token"
access_token_secret <- "access_token_secret"
options(httr_oauth_cache=T)
setup_twitter_oauth(api_key,api_secret,access_token,access_token_secret)
searchResult <- searchTwitter('#GoodMorning', n=1, lang = 'en')
tweetDetailsDF <- twListToDF(searchResult)

if(!tweetDetailsDF$isRetweet) {
updateStatus(paste0("@", tweetDetailsDF$screenName, " Good Morning, Have a nice day! :-) "), inReplyTo = tweetDetailsDF$id)
}
  
