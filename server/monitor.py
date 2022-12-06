from pymongo import MongoClient 
import json 
from threading import Thread
import time
import send as send
import os
uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
                'uni', 'uni1234', 'db.yoonleeverse.com')
client=MongoClient(uri)
def monitor():
    db=client['UniMarketDB']
    collection=db['data']
    collection2=db['UserDB']
    for post in collection2.find():
        monitor_collection=db["{}".format(post['user_id'])]
        data=[]
        for i in monitor_collection.find():
            data.append(i)
        for i in collection.find({'$and':[{'$and':[{"price":{"$lte":post['max_price']}},{"price":{"$gte":post['min_price']}},
        {"title":{"$regex":".*{}.*".format(post['title'])}}]},{'$nor':[{"title":{"$regex":".*{}.*".format(post['filter_keyword'])}},
        {"region":{"$regex":".*{}.*".format(post['region'])}}]}]}):#갱신된 부분이 있는지 확인
            if i['item_id'] not in data:
                    send(post['user_id'],i['title'])
                    # 알림 보내기
                    monitor_collection.insert_one(i['item_id'])