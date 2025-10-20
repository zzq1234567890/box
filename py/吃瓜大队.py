# coding=utf-8

# !/usr/bin/python

import sys

import requests

from bs4 import BeautifulSoup

import re

import json

from base.spider import Spider



sys.path.append('..')

xurl = "https://i.cgdd27.buzz"

headerx = {

    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36'

}

class Spider(Spider):

    global xurl

    global headerx



    def getName(self):

        return "首页"



    def init(self, extend):

        pass



    def isVideoFormat(self, url):

        pass



    def manualVideoCheck(self):

        pass



    def fl(self,key):

        videos = []

        doc = BeautifulSoup(key, "html.parser")

        soup = doc.find_all('article')

        for vods in soup:

            name = vods.select_one("a img")['alt']

            id = vods.select_one("a")["href"]

            pic = vods.select_one("a img ")["data-src"]

            remark = vods.find('time').get_text()

            video = {

                "vod_id": id,

                "vod_name": name,

                "vod_pic": pic,

                "vod_remarks": '更新时间:' + remark

            }

            videos.append(video)

        return videos



    def homeContent(self, filter):

        result = {}

        result['class'] = []

        result['class'].append({'type_id': 'qiwenyishi', 'type_name': '奇闻异事'})

        result['class'].append({'type_id': 'fanchanvyou', 'type_name': '反差女友'})

        result['class'].append({'type_id': 'wanghongmingxing', 'type_name': '网红明星'})

        result['class'].append({'type_id': 'xiaoyuanshijian', 'type_name': '校园事件'})

        return result



    def homeVideoContent(self):

        detail = requests.get(url=xurl, headers=headerx, allow_redirects=False)

        detail.encoding = "utf-8"

        res = detail.text

        videos = self.fl(res)

        result = {'list': videos}

        return result



    def categoryContent(self, cid, pg, filter, ext):        

        result = {}

        if not pg:

            pg = 1

        videos = []

        try:

            url = 'https://i.cgdd27.buzz/category/' + cid + '/page/' + str(pg)

            res = requests.get(url, headers=headerx)

            res.encoding = "utf-8"

            res = res.text

            videos = self.fl(res)

            result = {'list': videos}



        except:

            pass



        result['list'] = videos

        result['page'] = pg

        result['pagecount'] = 9999

        result['limit'] = 90

        result['total'] = 999999

        return result



    def detailContent(self, ids):

        did = ids[0]

        videos = []

        result = {}



        videos.append({

            "vod_id": '',

            "vod_name": '',

            "vod_pic": "",

            "type_name": "ぃぅおか🍬 คิดถึง",

            "vod_year": "",

            "vod_area": "",

            "vod_remarks": "",

            "vod_actor": "",

            "vod_director": "",

            "vod_content": "",

            "vod_play_from": "直链播放",

            "vod_play_url": did

        })



        result['list'] = videos

        return result



    def playerContent(self, flag, id, vipFlags):

        result = {}

        res = requests.get(id, headers=headerx)

        res.encoding = "utf-8"

        match = re.search(r'controls><source src="(.*?)"', res.text)



        if match:

            purl = match.group(1).replace('\\', '')

        result["parse"] = 0

        result["playUrl"] = ''

        result["url"] = purl

        result["header"] = headerx

        return result



    def searchContentPage(self, key, quick, page):

        result = {}

        videos = []

        if not page:

            page = 1

        url = 'https://i.cgdd27.buzz/page/' + str(page) + '?s=' + key

        res = requests.get(url, headers=headerx)

        res.encoding = "utf-8"

        res = res.text

        videos = self.fl(res)



        result['list'] = videos

        result['page'] = page

        result['pagecount'] = 9999

        result['limit'] = 90

        result['total'] = 999999

        return result





    def searchContent(self, key, quick):

        return self.searchContentPage(key, quick, '1')







    def localProxy(self, params):

        if params['type'] == "m3u8":

            return self.proxyM3u8(params)

        elif params['type'] == "media":

            return self.proxyMedia(params)

        elif params['type'] == "ts":

            return self.proxyTs(params)

        return None
