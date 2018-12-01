from lxml import etree

text = '''<ul class="ulist focuslistnews">
<li class="bold-item">
<span class="dot"></span>
<a href="https://xinwen.eastday.com/a/n181130123459788.html?qid=news.baidu.com" mon="ct=1&amp;a=2&amp;c=top&amp;pn=1" target="_blank" class=""></a></li>
<li class="">
<a href="https://3w.huanqiu.com/a/7ab55a/7IflcL5g7Ty?agt=8" mon="ct=1&amp;a=2&amp;c=top&amp;pn=2" target="_blank" class=" xh-highlight">财政部:跨境电商零售进口单次交易限值将提至5千元</a></li>
<li class="">
<a href="https://xinwen.eastday.com/a/181130043744023.html?qid=news.baidu.com" mon="ct=1&amp;a=2&amp;c=top&amp;pn=3" target="_blank" class="">油价迎年内首个“三连跌”,加满一箱油将少花逾20元</a></li>
<li class="">
<a href="https://tech.ifeng.com/c/7iEYh4nDm9g?_zbs_baidu_news" mon="ct=1&amp;a=2&amp;c=top&amp;pn=4" target="_blank" class="">华为徐直军：没有我们的参与 美国或无法赢得5G竞赛</a></li>
<li class="">
<a href="http://world.chinadaily.com.cn/wykzg/2018-11/30/content_37337133.htm" mon="ct=1&amp;a=2&amp;c=top&amp;pn=5" target="_blank" class="">2018阿根廷世界小姐为中国"代言":这里美得让人流连忘返</a></li>
<li class="">
<a href="https://xinwen.eastday.com/a/n181130073727130.html?qid=news.baidu.com" mon="ct=1&amp;a=2&amp;c=top&amp;pn=6" target="_blank" class="">多省晒“家底”！广东近13万亿 海南超万亿</a>
</ul>'''

html = etree.HTML(text)
print(html)

# 查看element对象中包含的字符串,解决了中文不能显示的问题

# print(etree.tostring(html,encoding = "utf-8",pretty_print = True,method = "html").decode())
    
# 获取ul中class为  “ulist focuslistnews”的a的 href网址
ret1 = html.xpath("//ul[@class='ulist focuslistnews']//a/@href")
# print(ret1)

# 获取每条新闻的标题
ret2 = html.xpath("//ul[@class='ulist focuslistnews']//a/text()")
# print(ret2)

# 将两个ret放在一起作为字典

# for href in ret1:
#     item = {}
#     item["href"] = href
#     item["title"] = ret2[ret1.index(href)]
#     print(item)
print("*"*20)

# 排除数据里的“None”
ret3 = html.xpath("//ul[@class='ulist focuslistnews']//a")
for i in ret3:
    item = {}
    
    item["title"] = i.xpath("./text()")[0] if len(i.xpath("./text()"))>0 else None
    item["href"] = i.xpath("./@href")[0] if len(i.xpath("./@href"))>0 else None
    print(item)





