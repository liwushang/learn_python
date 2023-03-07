import json
data = [{"name": "laowang", "age": 16}, {"name": "zhangsan", "age": 20}]
data = json.dumps(data)
print(data, type(data))
data = json.loads(data)
print(data, type(data))
