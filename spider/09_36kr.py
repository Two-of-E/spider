from parse_url import parse_url
import re
import json

url = "https://36kr.com/"

html_str = parse_url(url)

ret = re.findall("<script>var props=(.*?),locationnal=",html_str)0[]

with open("36kr.json","w",encoding="utf-8") as f:
    f.write(ret)

ret = json.loads(ret)

print(ret)
