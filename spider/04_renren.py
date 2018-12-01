import requests

session = requests.session()
post_url = "http://www.renren.com/PLogin.do"
post_data = {"email":"15032393105","password":"521zxcwsx"}

headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
session.post(post_url,data=post_data,headers=headers)

r = session.get("http://www.renren.com/968910895/profile",headers=headers)



with open("renren1.html","w",encoding="utf-8") as f:
    f.write(r.content.decode())



