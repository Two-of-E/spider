# 逐层爬取贴吧
import requests
from lxml import etree


class TiebaSpider:
    def __init__(self,tieba_name):
        self.start_url = "http://tieba.baidu.com/mo/q---1E1A44492752A8CFE48A31DB2C0BB8FE:FG=1--1-3-0--2--wapp_1536855175546_700/m?kw="+tieba_name+"&pn=10"
        self.headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
    def paral_url(self):
        response = requests.get(url,headers = self.headers)
        return response.content.decode()

    def get_content_list(self,html_str):
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[contain(class,'i')]")
        for div


    def run(self):
        # 1.start_url
        # 2.发送请求，获取响应
        # 3.提取数据，提取下一页的url地址
            # 3.1提取列表页的url地址和标题
            # 3.2请求列表页的url地址，获取详情页的第一页
            # 3.3提取详情页第一页的图片，提取下一页的地址
            # 3.4请求详情页下一页的地址，进入循环3.2 - 3.4，也就是循环提取图片
        # 4.保存数据
        # 5.请求下一页的url地址，进入循环2-5，








