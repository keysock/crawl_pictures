import random

import requests
import os
import re
from datetime import datetime
if not os.path.exists('./img/multipleImg'):
    os.mkdir('./img/multipleImg')

headers = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Cookie': 'BAIDUID=BFDBC07BE9391AAB59C9D1EA05DB2E0E:FG=1; BIDUPSID=BFDBC07BE9391AAB44D8B72F4BC485E0; PSTM=1632295491; __yjs_duid=1_63c2a3b4e2ca88064182603d388c1cec1634276177182; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; MCITY=-179%3A158%3A; ab_sr=1.0.1_NjM3NmI5OWUzNDI3NzNjYWY4MThkZGRhMDc5YWI5YTBjODNjOGY4ZjdhMWEwNTBiNDQ0NTFmMDhmM2Q5NTc0NzM3MDhiNzY3OTVmNWVlNWNhY2YzYzA2NGYyZGM3MGY3NjI0YTllZDQ2ZGE5ZThiNWQ1ZDQ0NTg4MjQ1MzE3ZmY3MjZhYjZkMTYyNTNmNTUwMmE1NTQwYTMyYTMxMzNhNQ==; BA_HECTOR=8h2ga5a4048k24almm1h5cg0r0q; BDRCVFR[Fc9oatPmwxn]=srT4swvGNE6uzdhUL68mv3; delPer=0; PSINO=7; H_PS_PSSID=35836_36178_31254_36020_34812_35914_36166_34584_36120_35978_36126_36236_26350_36091_36061; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=ala; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
}
# url='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1649830537625_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MCwzLDIsMSw0LDUsNyw2LDgsOQ%3D%3D&ie=utf-8&sid=&word=%E5%A4%A7%E8%83%B8%E5%A6%B9'
url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C3%C0%C5%AE&fr=ala&ala=1&alatpl=normal&pos=0&dyTabStr=MCwzLDIsMSw0LDUsNyw2LDgsOQ%3D%3D'
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
images_text = response.text
with open('images.html','w',encoding='utf-8') as f:
    f.write(images_text)
ex='"objURL":"(.*?)"'
imges_src_list = re.findall(ex, images_text, re.S)
print(imges_src_list)
i=0
for img in imges_src_list:
    url=f'{img}'
    response=requests.get(url=url,headers=headers)
    img_data=response.content
    # print(img.split('%'))
    imgName=str(datetime.now().strftime('%Y%m%d%H%M%S'))+str(random.randint(1000,10000))+f'美女图片{i}.jpg'
    # print(imgName)
    # imgName=f'meinvtupian{i}.jpg'
    i+=1
    imgPath='./img/multipleImg/'+imgName
    with open(imgPath,'wb') as f:
        f.write(img_data)
    print(imgName,'抓取成功！！！')
