# coding=utf-8
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}

# p = {"wd":"传智博客"}

# url_temp = "https://www.baidu.com/s?"

# r = requests.get(url_temp,headers=headers,params=p)

# print(r.status_code)
# print(r.request.url)

# 这里用到了format()语法，格式化字符串
url = "https://www.baidu.com/s?wd={}".format("传智播客")
r = requests.get(url, headers=headers)
print(r.status_code)
print(r.request.url)

r = requests.get("https://movie.douban.com/j/search_subjects?type=tv&tag=英剧&sort=recommend&page_limit=20&page_start=0",headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"})
