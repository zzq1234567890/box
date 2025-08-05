# -*- coding: utf-8 -*-
# @Author  : Doubebly
# @Time    : 2025/5/19 21:19

import sys
import requests
import base64
import os
import time
sys.path.append('..')
from base.spider import Spider


class Spider(Spider):
    def getName(self):
        return "BeeSport"

    def init(self, extend):
        self.ext_time = 120
        self.cache_path = '/storage/emulated/0/TV/cache_BeeSport'
        if not os.path.exists(self.cache_path):
            os.mkdir(self.cache_path, 0o755)
        pass

    def getDependence(self):
        return []

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass


    def liveContent(self, url):
        data_list = [{'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/TNT_SPORTS_1.png', 'group-title': 'BeeSport', 'name': 'TNT SPORTS 1', 'fun': 'beesports', 'pid': 'TNT_Sports_1'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/TNT_SPORTS_2.png', 'group-title': 'BeeSport', 'name': 'TNT SPORTS 2', 'fun': 'beesports', 'pid': 'TNT_Sports_2'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/TNT_SPORTS_3.png', 'group-title': 'BeeSport', 'name': 'TNT SPORTS 3', 'fun': 'beesports', 'pid': 'TNT_Sports_3'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/TNT_SPORTS_4.png', 'group-title': 'BeeSport', 'name': 'TNT SPORTS 4', 'fun': 'beesports', 'pid': 'TNT_Sports_4'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SKY_SPORTS_FOOTBALL.png', 'group-title': 'BeeSport', 'name': 'SKY SPORTS FOOTBALL', 'fun': 'beesports', 'pid': 'Sky_Sports_Football_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SKY_SPORTS_MAIN_EVENT.png', 'group-title': 'BeeSport', 'name': 'SKY SPORTS MAIN EVENT', 'fun': 'beesports', 'pid': 'Sky_Sports_Main_Event'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SKY_SPORTS_PREMIER_LEAGUE.png', 'group-title': 'BeeSport', 'name': 'SKY SPORTS PREMIER LEAGUE', 'fun': 'beesports', 'pid': 'Sky_Sports_Premier_League'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SKY_SPORTS_ACTION.png', 'group-title': 'BeeSport', 'name': 'SKY SPORTS ACTION', 'fun': 'beesports', 'pid': 'Sky_Sports_Action_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SKY_SPORTS_MIX.png', 'group-title': 'BeeSport', 'name': 'SKY SPORTS MIX', 'fun': 'beesports', 'pid': 'Sky_Sports_Mix_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SKY_SPORTS_ARENA.png', 'group-title': 'BeeSport', 'name': 'SKY SPORTS ARENA', 'fun': 'beesports', 'pid': 'Sky_Sports_Arena_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SKY_SPORTS_NEWS.png', 'group-title': 'BeeSport', 'name': 'SKY SPORTS NEWS', 'fun': 'beesports', 'pid': 'Sky_Sports_News_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SKY_SPORTS_CRICKET.png', 'group-title': 'BeeSport', 'name': 'SKY SPORTS CRICKET', 'fun': 'beesports', 'pid': 'Sky_Sports_Cricket_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Sky_Sports_Tennis.png', 'group-title': 'BeeSport', 'name': 'Sky Sports Tennis', 'fun': 'beesports', 'pid': 'Sky_Sports_Tennis'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SKY_SPORTS_F1.png', 'group-title': 'BeeSport', 'name': 'SKY SPORTS F1', 'fun': 'beesports', 'pid': 'Sky_Sports_F1_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SKY_SPORTS_GOLF.png', 'group-title': 'BeeSport', 'name': 'SKY SPORTS GOLF', 'fun': 'beesports', 'pid': 'Sky_Sports_Golf_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SKY_SPORTS_RACING.png', 'group-title': 'BeeSport', 'name': 'SKY SPORTS RACING', 'fun': 'beesports', 'pid': 'Sky_Sports_Racing_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Sky_Sports_Darts.png', 'group-title': 'BeeSport', 'name': 'Sky Sports Darts', 'fun': 'beesports', 'pid': 'Sky_Sports_Darts'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/BEIN_SPORTS_USA.png', 'group-title': 'BeeSport', 'name': 'BEIN SPORTS USA', 'fun': 'beesports', 'pid': 'Bein_Sports_USA_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/TENNIS_CHANNEL.png', 'group-title': 'BeeSport', 'name': 'TENNIS CHANNEL', 'fun': 'beesports', 'pid': 'Tennis_Channel_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/LALIGA_TV_HD.png', 'group-title': 'BeeSport', 'name': 'LALIGA TV HD', 'fun': 'beesports', 'pid': 'La_Liga_TV_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/HBO_1.png', 'group-title': 'BeeSport', 'name': 'HBO 1', 'fun': 'beesports', 'pid': 'HBO_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/HBO_2.png', 'group-title': 'BeeSport', 'name': 'HBO 2', 'fun': 'beesports', 'pid': 'HBO_2_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Discovery_Channel.png', 'group-title': 'BeeSport', 'name': 'Discovery Channel', 'fun': 'beesports', 'pid': 'Discovery_Channel_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Discovery_Life.png', 'group-title': 'BeeSport', 'name': 'Discovery Life', 'fun': 'beesports', 'pid': 'Discovery_Life_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Cinemax_West.png', 'group-title': 'BeeSport', 'name': 'Cinemax West', 'fun': 'beesports', 'pid': 'Cinemax_West_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Great_Movies.png', 'group-title': 'BeeSport', 'name': 'Great Movies', 'fun': 'beesports', 'pid': 'UK_Great_Movies_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Sky_Cinema_Comedy.png', 'group-title': 'BeeSport', 'name': 'Sky Cinema Comedy', 'fun': 'beesports', 'pid': 'UK_Sky_Cinema_Comedy_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Sky_Cinema_Family.png', 'group-title': 'BeeSport', 'name': 'Sky Cinema Family', 'fun': 'beesports', 'pid': 'UK_Sky_Cinema_Family_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Cartoon_Network.png', 'group-title': 'BeeSport', 'name': 'Cartoon Network', 'fun': 'beesports', 'pid': 'UK_Cartoon_Network_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Virgin_2.png', 'group-title': 'BeeSport', 'name': 'Virgin 2', 'fun': 'beesports', 'pid': 'UK_Virgin_2'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Virgin_3.png', 'group-title': 'BeeSport', 'name': 'Virgin 3', 'fun': 'beesports', 'pid': 'UK_Virgin_3'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Virgin_1.png', 'group-title': 'BeeSport', 'name': 'Virgin 1', 'fun': 'beesports', 'pid': 'UK_Virgin_1'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Bein_Sports_English_2.png', 'group-title': 'BeeSport', 'name': 'Bein Sports English 2', 'fun': 'beesports', 'pid': 'Bein_Sports_English_2_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SuperSport_Premier_League.png', 'group-title': 'BeeSport', 'name': 'SuperSport Premier League', 'fun': 'beesports', 'pid': 'SuperSport_Premier_League_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SuperSport_LaLiga.png', 'group-title': 'BeeSport', 'name': 'SuperSport LaLiga', 'fun': 'beesports', 'pid': 'SuperSport_LaLiga_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SuperSport_Action.png', 'group-title': 'BeeSport', 'name': 'SuperSport Action', 'fun': 'beesports', 'pid': 'SuperSport_Action_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SuperSport_Blitz.png', 'group-title': 'BeeSport', 'name': 'SuperSport Blitz', 'fun': 'beesports', 'pid': 'SuperSport_Blitz_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SuperSport_Cricket.png', 'group-title': 'BeeSport', 'name': 'SuperSport Cricket', 'fun': 'beesports', 'pid': 'SuperSport_Cricket_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SuperSport_Football.png', 'group-title': 'BeeSport', 'name': 'SuperSport Football', 'fun': 'beesports', 'pid': 'SuperSport_Football_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SuperSport_Golf.png', 'group-title': 'BeeSport', 'name': 'SuperSport Golf', 'fun': 'beesports', 'pid': 'SuperSport_Golf_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SuperSport_Rugby.png', 'group-title': 'BeeSport', 'name': 'SuperSport Rugby', 'fun': 'beesports', 'pid': 'SuperSport_Rugby_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/SuperSport_Tennis.png', 'group-title': 'BeeSport', 'name': 'SuperSport Tennis', 'fun': 'beesports', 'pid': 'SuperSport_Tennis_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Variety_1.png', 'group-title': 'BeeSport', 'name': 'Variety 1', 'fun': 'beesports', 'pid': 'Variety_1_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Variety_2.png', 'group-title': 'BeeSport', 'name': 'Variety 2', 'fun': 'beesports', 'pid': 'Variety_2_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Variety_3.png', 'group-title': 'BeeSport', 'name': 'Variety 3', 'fun': 'beesports', 'pid': 'Variety_3_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Variety_4.png', 'group-title': 'BeeSport', 'name': 'Variety 4', 'fun': 'beesports', 'pid': 'Variety_4_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Eurosport_1.png', 'group-title': 'BeeSport', 'name': 'Eurosport 1', 'fun': 'beesports', 'pid': 'Eurosport_1_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Eurosport_2.png', 'group-title': 'BeeSport', 'name': 'Eurosport 2', 'fun': 'beesports', 'pid': 'Eurosport_2_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Premier_Sports_1.png', 'group-title': 'BeeSport', 'name': 'Premier Sports 1', 'fun': 'beesports', 'pid': 'Premier_Sports_1'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Premier_Sports_2.png', 'group-title': 'BeeSport', 'name': 'Premier Sports 2', 'fun': 'beesports', 'pid': 'Premier_Sports_2'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Golf_Channel.png', 'group-title': 'BeeSport', 'name': 'Golf Channel', 'fun': 'beesports', 'pid': 'Golf_Channel_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/MLB_Network.png', 'group-title': 'BeeSport', 'name': 'MLB Network', 'fun': 'beesports', 'pid': 'MLB_Network_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/NBA_TV.png', 'group-title': 'BeeSport', 'name': 'NBA TV', 'fun': 'beesports', 'pid': 'NBA_TV_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/NFL_Network.png', 'group-title': 'BeeSport', 'name': 'NFL Network', 'fun': 'beesports', 'pid': 'NFL_Network_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/NFL_REDZONE.png', 'group-title': 'BeeSport', 'name': 'NFL REDZONE', 'fun': 'beesports', 'pid': 'NFL_REDZONE_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/NHL_Network.png', 'group-title': 'BeeSport', 'name': 'NHL Network', 'fun': 'beesports', 'pid': 'NHL_Network_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/WWE.png', 'group-title': 'BeeSport', 'name': 'WWE', 'fun': 'beesports', 'pid': 'WWE_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Willow_Cricket.png', 'group-title': 'BeeSport', 'name': 'Willow Cricket', 'fun': 'beesports', 'pid': 'Willow_Cricket_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Willow_Extra.png', 'group-title': 'BeeSport', 'name': 'Willow Extra', 'fun': 'beesports', 'pid': 'Willow_Extra_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/World_Fishing_Network.png', 'group-title': 'BeeSport', 'name': 'World Fishing Network', 'fun': 'beesports', 'pid': 'World_Fishing_Network_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/ESPN.png', 'group-title': 'BeeSport', 'name': 'ESPN', 'fun': 'beesports', 'pid': 'ESPN_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/ESPN_2.png', 'group-title': 'BeeSport', 'name': 'ESPN 2', 'fun': 'beesports', 'pid': 'ESPN_2_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/ESPN_News.png', 'group-title': 'BeeSport', 'name': 'ESPN News', 'fun': 'beesports', 'pid': 'ESPN_News_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/ESPN_U.png', 'group-title': 'BeeSport', 'name': 'ESPN U', 'fun': 'beesports', 'pid': 'ESPN_U_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/ITV_1.png', 'group-title': 'BeeSport', 'name': 'ITV 1', 'fun': 'beesports', 'pid': 'ITV_1'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/ITV_2.png', 'group-title': 'BeeSport', 'name': 'ITV 2', 'fun': 'beesports', 'pid': 'ITV_2'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/ITV_3.png', 'group-title': 'BeeSport', 'name': 'ITV 3', 'fun': 'beesports', 'pid': 'ITV_3'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/ITV_4.png', 'group-title': 'BeeSport', 'name': 'ITV 4', 'fun': 'beesports', 'pid': 'ITV_4'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/MUTV.png', 'group-title': 'BeeSport', 'name': 'MUTV', 'fun': 'beesports', 'pid': 'MUTV_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/LFC_TV.png', 'group-title': 'BeeSport', 'name': 'LFC TV', 'fun': 'beesports', 'pid': 'LFC_TV_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/FOX_NEWS.png', 'group-title': 'BeeSport', 'name': 'FOX NEWS', 'fun': 'beesports', 'pid': 'FOX_NEWS_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/ACC_Network.png', 'group-title': 'BeeSport', 'name': 'ACC Network', 'fun': 'beesports', 'pid': 'ACC_Network_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Fight_Network.png', 'group-title': 'BeeSport', 'name': 'Fight Network', 'fun': 'beesports', 'pid': 'Fight_Network_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/CBS_Sports_Network.png', 'group-title': 'BeeSport', 'name': 'CBS Sports Network', 'fun': 'beesports', 'pid': 'CBS_Sports_Network_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/CNBC.png', 'group-title': 'BeeSport', 'name': 'CNBC', 'fun': 'beesports', 'pid': 'CNBC_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Fox_Sports_1.png', 'group-title': 'BeeSport', 'name': 'Fox Sports 1', 'fun': 'beesports', 'pid': 'Fox_Sports_1_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Fox_Sports_2.png', 'group-title': 'BeeSport', 'name': 'Fox Sports 2', 'fun': 'beesports', 'pid': 'Fox_Sports_2_Live_TV'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/Nat_Geo_Wild_HD.png', 'group-title': 'BeeSport', 'name': 'Nat Geo Wild HD', 'fun': 'beesports', 'pid': 'Nat_Geo_Wild_HD'}, {'tvg-id': '', 'tvg-name': '', 'tvg-logo': 'https://logo.doube.eu.org/beesports/ABC_Channel.png', 'group-title': 'BeeSport', 'name': 'ABC Channel', 'fun': 'beesports', 'pid': 'ABC'}]

        tv_list = ['#EXTM3U']
        for i in data_list:
            tvg_id = i['tvg-id']
            tvg_name = i['tvg-name']
            tvg_logo = i['tvg-logo']
            group_name = i['group-title']
            name = i['name']
            fun = i['fun']
            pid = i['pid']
            tv_list.append(f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-name="{tvg_name}" tvg-logo="{tvg_logo}" group-title="{group_name}",{name}')
            tv_list.append(f'{self.getProxyUrl()}&fun={fun}&pid={pid}&Author=Doubebly&TG=t.me/doubebly001')

        return '\n'.join(tv_list)

    def homeContent(self, filter):
        return {}

    def homeVideoContent(self):
        return {}

    def categoryContent(self, cid, page, filter, ext):
        return {}

    def detailContent(self, did):
        return {}

    def searchContent(self, key, quick, page='1'):
        return {}

    def searchContentPage(self, keywords, quick, page):
        return {}

    def playerContent(self, flag, pid, vipFlags):
        return {}

    def localProxy(self, params):
        _fun = params.get('fun', None)
        _type = params.get('type', None)
        if _fun is not None:
            fun = getattr(self, f'fun_{_fun}')
            return fun(params)
        return [302, "text/plain", None, {'Location': 'https://sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/mp4/xgplayer-demo-720p.mp4'}]


    def fun_beesports(self, params):
        pid = params['pid']
        cache_play_url = self.cache_get(pid)
        if cache_play_url != 'False':
            return [302, "text/plain", None, {'Location': cache_play_url}]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'origin': 'https://beesports.net',
            'referer': 'https://beesports.net/live-tv',
        }

        json_data = {
            'channel': f'https://live_tv.starcdnup.com/{pid}/index.m3u8',
        }
        try:
            response = requests.post('https://beesports.net/authorize-channel', headers=headers, json=json_data)
            url = response.json()['channels'][0]
            self.cache_set(pid, url)
            return [302, "text/plain", None, {'Location': url}]
        except Exception as e:
            return [302, "text/plain", None, {'Location': 'https://sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/mp4/xgplayer-demo-720p.mp4'}]

    def destroy(self):
        files_and_dirs = os.listdir(self.cache_path)
        if len(files_and_dirs) > 0:
            for file in files_and_dirs:
                os.remove(os.path.join(self.cache_path, file))
        return '正在Destroy'

    def b64encode(self, data):
        return base64.b64encode(data.encode('utf-8')).decode('utf-8')

    def b64decode(self, data):
        return base64.b64decode(data.encode('utf-8')).decode('utf-8')


    def cache_get(self, key):
        t = time.time()
        path = self.cache_getkey(key)
        if not os.path.exists(path):
            return 'False'
        if t - os.path.getmtime(path) > self.ext_time:
            return 'False'
        with open(path, 'r', encoding='utf-8') as f:
            data = f.read()
        return data

    def cache_set(self, key, data):
        path = self.cache_getkey(key)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(data)
        return True

    def cache_getkey(self, key):
        return self.cache_path + '/' + key + '.txt'

if __name__ == '__main__':
    pass
