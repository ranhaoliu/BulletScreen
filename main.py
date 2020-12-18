"""docstring for Bilibili"""
import time


import requests
from lxml import etree

from 弹幕.oid_.Oid import Oid


class Bilibili():
 def __init__(self, av_id):
    self.headers = {
        'Host': 'api.bilibili.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'finger=edc6ecda; LIVE_BUVID=AUTO1415378023816310; stardustvideo=1; CURRENT_FNVAL=8; buvid3=0D8F3D74-987D-442D-99CF-42BC9A967709149017infoc; rpdid=olwimklsiidoskmqwipww; fts=1537803390'

    }
    self.oid = Oid(av_id).get_oid()
    # print(self.oid)
    self.url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=' + self.oid
    self.barrage_reault = self.get_page()


# 获取信息
 def get_page(self):
    try:
        # 延时操作，防止太快爬取
        time.sleep(0.5)
        response = requests.get(self.url, headers=self.headers)
    except Exception as e:
        print('获取xml内容失败,%s' % e)
        return False
    else:
        if response.status_code == 200:
            # 下载xml文件
            with open('bilibili.xml', 'wb') as f:
                f.write(response.content)
            return True
        else:
            return False


# 解析网页
 def param_page(self):
    time.sleep(1)
    if self.barrage_reault:
        # 文件路径，html解析器
        html = etree.parse('bilibili.xml', etree.HTMLParser())
        # xpath解析，获取当前所有的d标签下的所有文本内容
        results = html.xpath('//d//text()')
        return results
# b=Bilibili("BV1cy4y1k7A2")
id = input("请输入b栈的视频id号:")
b=Bilibili(id)
danmu_result = b.param_page()
print(danmu_result)