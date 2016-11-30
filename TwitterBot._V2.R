library(twitteR)
api_key <- "api_key"
api_secret <- "api_secret"
access_token <- "access_token"
access_token_secret <- "access_token_secret"
options(httr_oauth_cache=T)
setup_twitter_oauth(api_key,api_secret,access_token,access_token_secret)

wakeupUser <- getUser("wakeupwithsmile")
followpeople <- setdiff(wakeupUser$getFollowerIDs(), wakeupUser$getFriendIDs())

unfollowpeople <- setdiff(wakeupUser$getFriendIDs(), wakeupUser$getFollowerIDs())

if(!identical(followpeople, character(0))) {
  command ="python"
  path2script="D:/create_friendships.py"
  sapply(followpeople, function(x) {
    allArgs = c(path2script, x)
    output = system2(command, args=allArgs, stdout=TRUE)
  })
  
}

if(!identical(unfollowpeople, character(0))) {
  command ="python"
  path2script="D:/destroy_friendships.py"
  sapply(followpeople, function(x) {
    allArgs = c(path2script, x)
    output = system2(command, args=allArgs, stdout=TRUE)
  })
}

searchResult <- searchTwitter('#GoodMorning', n=1, lang = 'en')
tweetDetailsDF <- twListToDF(searchResult)

if(!tweetDetailsDF$isRetweet) {
updateStatus(paste0("@", tweetDetailsDF$screenName, " Good Morning, Have a nice day! :-) "), inReplyTo = tweetDetailsDF$id)
}
  