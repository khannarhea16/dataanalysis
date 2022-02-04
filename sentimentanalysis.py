
import requests
from textblob import TextBlob

# Bearer token from twitter developer account
bearer = ""

def connect_to_twitter():
    bearer_token = bearer
    return {"Authorization": "Bearer {}".format(bearer_token)}

def make_request(headers, searchterm):
    url = "https://api.twitter.com/2/tweets/search/recent?query={}".format(searchterm)
    return requests.request("GET", url, headers=headers).json()


def analyze(tweet):
  analysis = TextBlob(tweet)
  return analysis

headers = connect_to_twitter()
response = make_request(headers, "oscars")
positive = 0 
negative = 0 
neutral = 0 

for tweet in response['data']:
    result = analyze(tweet['text'])
    if result.sentiment.polarity > 0:
     positive = positive + 1
    elif result.sentiment.polarity == 0:
     neutral = neutral + 1
    else:
     negative = negative + 1
    
print("Positive {0}, Negative {1}, Neutral {2}".format(positive, negative, neutral))



