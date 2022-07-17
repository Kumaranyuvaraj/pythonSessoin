import json
data = {'jsonKey': 'jsonValue',"title": "hello world"}

d = json.dumps(data)
print(d)
print(type(d))