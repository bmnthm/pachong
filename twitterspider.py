import urllib.request
from bs4 import BeautifulSoup
import json

html = urllib.request.urlopen('https://twitter.com/realDonaldTrump').read()
soup = BeautifulSoup(html,"html.parser")
#print (soup)

spider_json = {}
'''
for string in soup.find_all('p',class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'):#推文内容
    string =  string.get_text()
    spider_json['content'] = string
    #print (spider_json['content'])
    json_str = json.dumps(spider_json)
    print(json_str.encode('utf-8').decode('unicode_escape'))

for string in soup.find_all('a',class_='tweet-timestamp js-permalink js-nav js-tooltip'):#推文日期
    string =  string.get('title')
    spider_json['date'] = string
    #print (spider_json['date'])
    json_str = json.dumps(spider_json)
    print(json_str.encode('utf-8').decode('unicode_escape'))
'''
for string in soup.find_all('span',class_='ProfileTweet-action--reply u-hiddenVisually'):#推文回复
    string =  string.get_text()
    spider_json['reply'] = string
    #print (spider_json['reply'])
    json_str = json.dumps(spider_json)
    print(json_str.encode('utf-8').decode('unicode_escape'))
'''
for string in soup.find_all('span',class_='ProfileTweet-action--retweet u-hiddenVisually'):#推文转发
    string =  string.get_text()
    spider_json['retweet'] = string
    #print (spider_json['retweet'])
    json_str = json.dumps(spider_json)
    print(json_str.encode('utf-8').decode('unicode_escape'))

for string in soup.find_all('span',class_='ProfileTweet-action--favorite u-hiddenVisually'):#推文点赞
    string =  string.get_text()
    spider_json['likes'] = string
    #print (spider_json['likes'])
    json_str = json.dumps(spider_json)
    print(json_str.encode('utf-8').decode('unicode_escape'))
'''