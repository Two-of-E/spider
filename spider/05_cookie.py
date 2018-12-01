import requests

# session = requests.session()
# post_url = "http://www.renren.com/PLogin.do"
# post_data = {"email":"61390869@qq.com","password":"521zxcwsx"}

headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}

cookies ="anonymid=jozrmvce-bxnvl7; depovince=HEB; _r01_=1; JSESSIONID=abcvhazoisi_l_l1ouvDw; ick_login=d80c5e59-03d5-43e7-8713-a176371efeb9; ick=5ca20dca-e9ef-4834-a1ea-525408833834; jebe_key=adba79ce-2e99-400d-973f-11473bc13744%7C20b8d994ffafd64059a300eb436c2a2b%7C1543324921129%7C1%7C1543324921135; ch_id=10050; __utma=151146938.2001429942.1543325503.1543325503.1543325503.1; __utmc=151146938; __utmz=151146938.1543325503.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; first_login_flag=1; ln_uact=15032393105; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; loginfrom=syshome; XNESSESSIONID=c7faa2db45ed; jebecookies=7c5bab48-205a-42a4-8000-e03031ed73c8|||||; _de=61556B610B3CD0AA246A1862394AD3A2; p=124d532056cb53ecd9df60086923907c5; t=72230279e6b84e94f1d0570aabb503d15; societyguester=72230279e6b84e94f1d0570aabb503d15; id=968910895; xnsid=aa813df5; wp_fold=0"

cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}

# session.post(post_url,data=post_data,headers=headers)

# r = session.get("http://www.renren.com/968910895/profile",headers=headers)

r = requests.get("http://www.renren.com/968910895/profile",headers=headers,cookies=cookies)

with open("renren1.html","w",encoding="utf-8") as f:
    f.write(r.content.decode())