import re
import json
import urllib
import urllib.request
import random

site = 'https://www.buxiaoshuai.com'
sitemaps = ['/sitemap.xml']

result = []
i=0

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  

for sitemap in sitemaps:
    sitemap = site+sitemap
    req = urllib.request.Request(url=sitemap, headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf-8')
    data = re.findall(re.compile(r'(?<=<loc>).*?(?=</loc>)'), html)
    result=result+data


del result[0]

googleUrllist=[]

for data in result:
    i=i+1
    result.remove(data)
    # baidu google 提交前50条
    googleUrllist.append(data)
    if i == 50:
        break

# baidu google 提交随机50条
if len(result) > 50:
    googleUrllist=googleUrllist + random.sample(result,50)
else:
    googleUrllist=googleUrllist + result

with open('urls.txt', 'w') as file:
    for data in googleUrllist:
        print(data, file=file)


# with open('all-urls.txt', 'w') as file:
#     for data in result:
#         print(data, file=file)
