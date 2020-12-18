import re
import requests
class Oid():
    def __init__(self,av_id):
        self.av_id=av_id
    def get_oid(self):
        # av_id:视频编号
        # av_id = 'BV1cy4y1k7A2'
        print("爬取视频编号为：{}".format(self.av_id))
        # 爬取视频页面html
        resp = requests.get('https://www.bilibili.com/video/' + self.av_id)
        # print(resp.text)
        #print(resp.text)
        #print("************")
        # 用正则表达式匹配到对应的oid（弹幕id）
        match_rule = r'cid=(.*?)&aid'
        oid = re.search(match_rule, resp.text).group().replace('cid=', '').replace('&aid', '')
        print('oid：' + oid)
        return oid
#b = Oid("av2051949")
#oid= b.get_oid()
#print("oid = {}".format(oid))