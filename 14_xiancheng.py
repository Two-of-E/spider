import requests
from lxml import etree
from lxml import Queue
import threading


class QiubaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()
    
    def get_url_list(self):
        for i in range(1,14):
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            print(url)
            response = requests.get(url,headers = self.headers)
            self.html_queue.put(response.content.decode())
            self.url_queue.task_done()

    def get_content_list(self):  # 提取数据
        while True:
            html_str = self.html_queue.get()
            html = etree.HTML(html_str)
            div_list = html.xpath("//div[@id='content-left']/div")
            content_list = []
            for div in div_list:
                item = {}
                item["content"] = div.xpath(".//div[@class='content']/span/text()")
                content_list.append(item)
            self.content_queue.put(content_list)
            self.html_queue.task_done()

    def save_content_list(self):
        while True:
            content_list = self.content_queue.get()
            for i in content_list:
               #  print(i)
            self.content_queue.task_done()
    
    def run(self):
        
        t_url = threading.Thread(target = self.get_url_list)
        thread_list.append(t_url)
        # 响应在等待时，可以分出时间去计算
        for i in range(5):
            t_parse = threading.Thread(target = self.parse_url)
            thread_list.append(t_parse)
        t_html = threading.Thread(target = self.get_content_list)
        thread_list.append(t_html)
        t_save = threading.Thread(target = self.save_content_list)
        thread_list.append(t_save)
        
        for t in thread_list:
            t.setDaemon(True)  # 子线程为守护线程，主线称结束子线程结束
            t.start()
        # 等待子线程结束
        for q in [self.url_queue,self.html_queue,self.content_queue]:
            q.join()

        print("主线程结束")
        # 1.url_list
        # 2.遍历，发送请求，获取响应
        # 3.提取数据
        #  # 4.保存




if __name__ == "__main__":
    qiubai= QiubaiSpider()
    qiubai.run()