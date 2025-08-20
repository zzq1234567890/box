import re
import requests
from lxml import etree, html
from base.spider import Spider


class Spider(Spider):

    def init(self, extend=""):
        pass

    def getName(self):
        return "HNYD VOD"

    def isVideoFormat(self, url):
        return False

    def manualVideoCheck(self):
        return False

    def destroy(self):
        pass

    def homeContent(self, filter):
        return {
            "class": [
                {"type_id": "tv", "type_name": "连续剧"},
                {"type_id": "movie", "type_name": "电影"},
                {"type_id": "variety", "type_name": "综艺"},
                {"type_id": "anime", "type_name": "动漫"},
            ],
            "list": [],
            "parse": 0,
            "jx": 0
        }

    def categoryContent(self, tid, pg, filter, extend):
        url = f"https://www.dbkk.cc/vtype/{tid}.html?page={pg}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
            "Referer": url,
        }

        try:
            resp = requests.get(url, headers=headers, timeout=30, verify=False, allow_redirects=True)
        except Exception:
            return {"list": [], "parse": 0, "jx": 0}

        if resp.status_code != 200 or not resp.text:
            return {"list": [], "parse": 0, "jx": 0}

        html_text = resp.content.decode("utf-8", errors="ignore")
        doc = etree.HTML(html_text)

        list_items = doc.xpath('//ul[contains(@class,"myui-vodlist")]/li')
        list_array = []

        for item in list_items:
            a_tag = item.xpath('.//a[contains(@class,"myui-vodlist__thumb")]')
            remarks_node = item.xpath('.//span[contains(@class,"pic-text text-right")]')

            if not a_tag:
                continue

            a_tag = a_tag[0]
            title = a_tag.get("title")
            href = a_tag.get("href")
            img_src = a_tag.get("data-original")

            remarks = remarks_node[0].text.strip() if remarks_node else ""

            vod_id = None
            m = re.search(r'/detail/(\d+)', href)
            if m:
                vod_id = m.group(1)
            else:
                m = re.search(r'/voddetail/(\d+)\.html', href)
                if m:
                    vod_id = m.group(1)

            if vod_id and title and img_src:
                list_array.append({
                    "vod_id": vod_id,
                    "vod_name": title,
                    "vod_pic": "https://www.dbkk.cc" + img_src,
                    "vod_remarks": remarks,
                })

        return {
            "list": list_array,
            "parse": 0,
            "jx": 0,
        }

    def detailContent(self, ids):
        ids = ids[0]
        target_url = f"https://www.dbkk.cc/detail/{ids}"

        headers = {
            "Referer": target_url,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
        }

        try:
            resp = requests.get(target_url, headers=headers, timeout=30, verify=False)
            resp.encoding = "utf-8"
            html_text = resp.text
        except Exception as e:
            return {"error": f"Failed to fetch HTML: {e}"}

        tree = html.fromstring(html_text)

        # 标题
        title = tree.xpath('//h1[@class="title"]/text()')
        title = title[0].strip() if title else ""

        # 年份
        year = tree.xpath('//p[@class="data"]//span[contains(text(),"年份")]/following-sibling::a[1]/text()')
        year = year[0].strip() if year else ""

        # 地区
        area = tree.xpath('//p[@class="data"]//span[contains(text(),"地区")]/following-sibling::a[1]/text()')
        area = area[0].strip() if area else ""

        # 演员
        actor_list = tree.xpath('//p[@class="data"]/span[contains(text(),"主演")]/following-sibling::a/text()')
        actor = " ".join([a.strip() for a in actor_list])

        # 导演
        director_list = tree.xpath('//p[@class="data"]/span[contains(text(),"导演")]/following-sibling::a/text()')
        director = " ".join([d.strip() for d in director_list])

        # 简介
        description = tree.xpath('//div[@id="desc"]//div[contains(@class,"content")]//p/text()')
        description = description[0].strip() if description else ""

        # 分类
        type_name = tree.xpath('//p[@class="data"]//span[contains(text(),"分类")]/following-sibling::a[1]/text()')
        type_name = type_name[0].strip() if type_name else ""

        # 集数列表
        play_urls = []
        episodes = tree.xpath('//ul[contains(@class,"myui-content__list")]/li/a')
        for ep in episodes:
            episode_title = ep.text_content().strip()
            episode_url = ep.get("href").strip()
            play_urls.append(f"{episode_title}${episode_url}")

        vod_play_url = "#".join(play_urls) if play_urls else ""

        return {
            "list": [{
                "type_name": type_name,
                "vod_id": ids,
                "vod_name": title,
                "vod_remarks": (description[:40] + "...") if description else "",
                "vod_year": year,
                "vod_area": area,
                "vod_actor": actor,
                "vod_director": director,
                "vod_content": description,
                "vod_play_from": "独播库",
                "vod_play_url": vod_play_url
            }],
            "parse": 0,
            "jx": 0
        }

    def playerContent(self, flag, id, vipFlags):
        vid = id.replace("-default", "-ep")

        # 替换 /play/xxx-epxx 为 /dbkp/xxx/exx
        vid = re.sub(r"/play/(\d+)-ep(\d+)", r"/dbkp/\1/ep\2", vid)

        # 进一步替换
        vid = vid.replace("play", "dbkp").replace("-", "/")

        url = "https://www.dbkk.cc" + vid

        headers = {
            "Referer": url,
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
            ),
            "Content-Type": "application/json;charset=utf-8"
        }

        try:
            resp = requests.get(url, headers=headers, timeout=30, verify=False)
            html_text = resp.text
        except Exception:
            return None

        # 匹配所有 m3u8
        matches = re.findall(r'url="([^"]+\.m3u8)"', html_text)
        if not matches:
            return None

        # 挨个检测可用性
        for test_url in matches:
            try:
                test_resp = requests.head(
                    test_url,
                    headers={
                        "User-Agent": headers["User-Agent"],
                        "Referer": url
                    },
                    allow_redirects=True,
                    timeout=10,
                    verify=False
                )
                if test_resp.status_code == 200:
                    return {"parse": 0, "jx": 0, "playUrl": "", "url": test_url, "header": headers}
            except Exception:
                continue

        return None

    def localProxy(self, param):
        return [200, "text/plain", "Hello from HNYD Spider!"]

    def liveContent(self, url):
        pass
