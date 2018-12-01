# coding=utf-8
#用百度翻译的接口翻译
import requests
import json
import sys

print(sys.argv)
query_string = sys.argv[1]

#headers = {"User-Agent":" Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}



post_data = {
    "query": query_string,
    "from": "en",
    "to": "zh",
}

post_url = "https://fanyi.baidu.com/basetrans"

r = requests.post(post_url, data=post_data, headers=headers)
# print(r.content.decode())
# print(1)

dict_ret = json.loads(r.content.decode())
ret = dict_ret["trans"][0]["dst"]
print("result is :",ret)


