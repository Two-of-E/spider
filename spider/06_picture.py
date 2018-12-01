import requests



headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}




r = requests.get("https://www.baidu.com/img/bd_logo1.png",headers=headers)
print(r.encoding)

with open("baidu.png","wb") as f:
    f.write(r.content)



