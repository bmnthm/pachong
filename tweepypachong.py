import tweepy  
import json

consumer_key = "dbWX9BdyoJW8qmQgLXkaEIxd4"  
consumer_secret = "Eh6DWR2bwm4LaeuinDxP98IN5NzEvq3COkQYQdmxhv6SUat0iK"  
access_token = "3120789387-KS6vfiMNcblLVkxGTEfa2ScYev8QntcBdLV0Htq"  
access_token_secret = "DWd3QquR9gqRQC7GAiQicjsq9AzpJVxEn3RdVHhqyuY1t"  

# 创建认证对象
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
# 设置你的access token和access secret
auth.set_access_token(access_token, access_token_secret)  
# 传入auth参数，创建API对象
api = tweepy.API(auth) 
spider_json = {}
# 使用API对象获取你的时间轴上的微博，并把结果存在一个叫做public_tweets的变量中
public_tweets = api.user_timeline(id="wanquribao")  
# 遍历所拉取的全部微博
for tweet in public_tweets:  
   # 打印存在微博对象中的text字段
   spider_json['content'] = tweet.text
   json_str = json.dumps(spider_json)
   print(json_str.encode('utf-8').decode('unicode_escape'))
   #print (tweet.text)