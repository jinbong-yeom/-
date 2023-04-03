from pymongo import MongoClient 
import json 
import time
from send import send
import os
from threading import Thread, Event

event = Event()
        uri = " " % (
                ' ', ' ', ' ')
client=MongoClient(uri)
def monitor():
    while(True):
        if event.is_set():
            return
        print("모니터링 중")
        db=client['UniMarketDB']
        collection=db['data']
        collection2=db['UserDB']
        for post in collection2.find():
            monitor_collection=db['{}'.format(post['user_id'])]
            data=[]
            for i in monitor_collection.find():
                data.append(i['item_id'])
            for i in collection.find({'$and':[{'$and':[{"price":{"$lte":post['max_price']}},{"price":{"$gte":post['min_price']}},
            {"title":{"$regex":".*{}.*".format(post['title'])}},{"region":{"$regex":".*{}.*".format(post['region'])}}]},
            {'$nor':[{"title":{"$regex":".*{}.*".format(post['filter_keyword'])}}]}]}):#갱신된 부분이 있는지 확인
                if i['item_id'] not in data:
                    send(post['firebase_id'],i['title'])
                    time.sleep(5)
                    # 알림 보내기
                    monitor_post={"item_id":i["item_id"]}
                    monitor_collection.insert_one(monitor_post)
        time.sleep(5)
