from flask import Flask, make_response, jsonify, request, make_response
from search import *
from monitor import *
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/posts/207092540')
def hello():
    test = {'userId': '207092540'}
    data = json.dumps(test, ensure_ascii=False).encode('utf8')
    
    return data


@app.route("/post",methods=['POST'])
def post():
    params = request.get_json()
    print(params)
    title = params['title']
    Max=params['filteringData']['maxPrice']
    Min=params['filteringData']['minPrice']
    Filter=params['filteringData']['excludeKeyword']
    result = search(title,Max,Min,Filter)
    print(result)
    return {"result":result}
'''
@app.route("/post",methods=['POST2'])
def post2():
    params = request.get_json()
    print(params)
    title = params['title']
    Max=params['filteringData']['maxPrice']
    Min=params['filteringData']['minPrice']
    Filter=params['filteringData']['excludeKeyword']
    result = monitor(title,Max,Min,Filter)
    print(result)
    return result
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=60000)