library(twitteR)
api_key <- "api_key "
api_secret <- "api_secret"
access_token <- "access_token"
access_token_secret <- "access_token_secret"
options(httr_oauth_cache=T)
setup_twitter_oauth(api_key,api_secret,access_token,access_token_secret)

library(httr)


library(RCurl)

postForm("https://api.twitter.com/1.1/friendships/create.json?user_id=101311381&follow=true", 
         .params = list(user_id = "101311381", follow = TRUE), .encoding = "json")

postForm("https://api.twitter.com/1.1/friendships/create", 
         .params = list(user_id = "101311381", follow = TRUE), .encoding = "json")

url <- "https://api.twitter.com/1.1/friendships/create.json"

POST(url, add_headers(Authorization = setup_twitter_oauth(api_key,api_secret,access_token,access_token_secret), 
     body = list(user_id = "101311381", follow = TRUE)))


b <- POST("https://api.twitter.com/1.1/friendships/create.json?user_id=101311381&follow=true")

url.create.friendships <- "https://api.twitter.com/1.1/friendships/create.json"
parametres <- "follow=true&user_id=101311381"
twitCred$OAuthRequest(URL=url.create.friendships,params=parametres)
library("ROAuth")

requestURL <- "https://api.twitter.com/oauth/request_token"
accessURL <- "https://api.twitter.com/oauth/access_token"
authURL <- "https://api.twitter.com/oauth/authorize"

twitCred <- OAuthFactory$new(consumerKey=api_key,
                             consumerSecret=api_secret, requestURL=requestURL, accessURL=accessURL,
                             authURL=authURL)

install.packages("jsonlite")
library(jsonlite)
fromJSON("https://api.twitter.com/1.1/friendships/create.json")


secret <- jsonlite::base64_enc(paste(api_key, api_secret, sep = ":"))
req <- httr::POST("https://api.twitter.com/oauth2/token",
                  httr::add_headers(
                    "Authorization" = paste("Basic", gsub("\n", "", secret)),
                    "Content-Type" = "application/x-www-form-urlencoded;charset=UTF-8"
                  ),
                  body = "grant_type=client_credentials"
);

httr::stop_for_status(req, "authenticate with twitter")
token <- paste("Bearer", httr::content(req)$access_token)
url <- "https://api.twitter.com/1.1/friendships/create.json?user_id=747311991283298310&follow=true"
b <- httr::POST(url, httr::add_headers(Authorization = token))


POST(url,config(token = setup_twitter_oauth(api_key,api_secret,access_token,access_token_secret)), httr::add_headers(Authorization = token))
url <- "https://api.twitter.com/1.1/friendships/create.json?user_id="
user_id <- 101311381

POST(url, verbose(), body = list(user_id = "747311991283298310"), encode = "json", httr::add_headers(Authorization = token))

POST(url, verbose(), body = list(user_id = 747311991283298310, follow = TRUE), encode = "json")


oauth_endpoints("twitter")

myapp <- oauth_app("twitter",key = "key",secret = "secret" ) 

twitter_token <- oauth1.0_token(oauth_endpoints("twitter"), myapp)

POST("https://api.twitter.com/1.1/friendships/create.json",
     query = list(user_id = 747311991283298310, follow = TRUE),
     config(token = setup_twitter_oauth(api_key,api_secret,access_token,access_token_secret))
)

POST("friendships/create", query = list(user_id = 747311991283298310, follow = TRUE))
new <- friendships(user_ids = c(101311381, 253814871))
new$following[1] <- TRUE
