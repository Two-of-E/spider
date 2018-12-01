import json
from parse_url import parse_url
from pprint import pprint


url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start=0&count=8&loc_id=108288&_=1543414789887"

html_str = parse_url(url)
# print(html_str)
ret1 = json.loads(html_str)
# pprint(ret1)
# print(type(ret1))

with open ("douban.json","w",encoding="utf-8") as f:
    f.write(json.dumps(ret1,ensure_ascii=False,indent=4))

# 还原字典函数
# with open("douban.json","r",encoding="utf-8") as f:
#     ret2 = f.read()
#     ret3 = json.loads(ret2)
#     print(ret3)
#     print(type(ret3))

#使用json.load 提取类文本文件对象中的数据
with open("douban.json","r",encoding="utf-8") as f:
    ret4 = json.load(f)
    print(ret4)


#json.dump将python类型放到类文件对象中
with open("douban.json","w",encoding="utf-8") as f:
    json.dump(ret1,f,ensure_ascii=False,indent=4)

