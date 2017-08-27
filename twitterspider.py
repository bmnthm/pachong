import urllib.request
from bs4 import BeautifulSoup
import json

html = urllib.request.urlopen('https://twitter.com/wanquribao').read()
soup = BeautifulSoup(html,"html.parser")
#print (soup)

i = 1

content_num = 1
date_num = 1
reply_num = 1
retweet_num = 1
likes_num = 1

content_dict = {}
date_dict = {}
reply_dict = {}
retweet_dict = {}
likes_dict = {}

spider_json = {}

for string in soup.find_all('p',class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'):#推文内容
    string =  string.get_text()
    content_dict[content_num] = string
    content_num += 1


for string in soup.find_all('a',class_='tweet-timestamp js-permalink js-nav js-tooltip'):#推文日期
    string =  string.get('title')
    date_dict[date_num] = string
    date_num += 1


for string in soup.find_all('span',class_='ProfileTweet-action--reply u-hiddenVisually'):#推文回复
    string =  string.get_text()
    reply_dict[reply_num] = string
    reply_num += 1


for string in soup.find_all('span',class_='ProfileTweet-action--retweet u-hiddenVisually'):#推文转发
    string =  string.get_text()
    retweet_dict[retweet_num] = string
    retweet_num += 1


for string in soup.find_all('span',class_='ProfileTweet-action--favorite u-hiddenVisually'):#推文点赞
    string =  string.get_text()
    likes_dict[likes_num] = string
    likes_num += 1


while i <= 20 :
    spider_json['content'] = content_dict[i]
    spider_json['date'] = date_dict[i]
    spider_json['reply'] = reply_dict[i]
    spider_json['retweet'] = retweet_dict[i]
    spider_json['likes'] = likes_dict[i]
    i += 1
    json_str = json.dumps(spider_json)
    print(json_str.encode('utf-8').decode('unicode_escape'))