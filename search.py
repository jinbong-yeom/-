from pymongo import MongoClient 
import json

uri = "" % (
                '', '', '')
client=MongoClient(uri)

db=client['UniMarketDB']
collection=db['data']
sanghan=300000
hahan=0
title="갤럭시"
one="S21"
two="S7"
three="무고"
item_id=[]# 기존 item_id
for i in collection.find():
      item_id.append(i['item_id'])
with open('item_id_list.txt','w',encoding='UTF-8')as f:
      for name in item_id:
            f.write(name+'\n')
for i in collection.find({'$and':[{'$and':[{"price":{"$lte":sanghan}},{"price":{"$gte":hahan}},
{"title":{"$regex":".*{}.*".format(title)}}]},{'$nor':[{"title":{"$regex":".*{}.*".format(one)}},
{"title":{"$regex":".*{}.*".format(two)}},{"title":{"$regex":".*{}.*".format(three)}}]}]}).sort("price"):
      print(i)