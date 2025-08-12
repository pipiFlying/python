"""
with open(path, mode='r+', encoding='utf-8') as f_r:

json.load(f_r)
    python 将 .json 文件解析成 python 可以处理的文件

json.loads(): python 解析 json 字符串

with open(path, mode='r+', encoding='utf-8') as f_w:

json.dump(obj, f_w, ensure_ascii=False, indent=4)
    python 将 python 存储成 .json 文件

json.dumps(): 将 python 数据转化成 json 字符串
"""

import json

with open('user.json', mode='r+', encoding='utf-8') as f:
    data = json.load(f)
    print(data)

json_str = '{ "name": "pipi", "age": 28 }'

json_obj = json.loads(json_str)

print(type(json_obj))
print(json_obj['name'])

dict_a = { 'id': 1, 'name': 'pipi', 'age': 28 }

dict_json = json.dumps(dict_a)

print(type(dict_json))
print(dict_json)


