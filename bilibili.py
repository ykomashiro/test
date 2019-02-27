"""
b站自动签到，关注up主与转发动态
"""

import time

import bs4
from lxml import etree
import requests
from selenium import webdriver

cookies = "l=v; LIVE_BUVID=AUTO5515350985011754; sid=5nsuzdo0; fts=1536252361; rpdid=iwiqmmpisldoskxisixww; UM_distinctid=165afe7b79262a-01a06cd4a717b8-9393265-100200-165afe7b793576; buvid3=109A25DC-0C78-4A69-B10F-757C7DBBFC2F149018infoc; im_notify_type_82747400=0; CURRENT_QUALITY=64; CURRENT_FNVAL=16; stardustvideo=0; im_local_unread_82747400=0; im_seqno_82747400=18; balh_server=https://www.biliplus.com; bp_t_offset_82747400=183675135409874175; finger=edc6ecda; DedeUserID=82747400; DedeUserID__ckMd5=4003f2425efe4a87; SESSDATA=df5e67c7%2C1544281084%2C28d37a04; bili_jct=eb5f954475de1abc268fbd45ca989c6b; _uuid=28401D7C-375A-69A2-A2BC-654E0FC2B09B95430infoc; _dfcaptcha=d93de83425323499dc0051bd533d9a66"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
url = "https://www.bilibili.com/"
headers = {'User-Agent': UA}


def get_cookies(original_cookies):
    cookies = dict()
    original_cookies = original_cookies.split('; ')
    for cookie in original_cookies:
        cookie = cookie.split('=')
        cookies[cookie[0]] = cookie[1]
    return cookies


cookies = get_cookies(cookies)
res = requests.get(url, cookies=cookies)
print(res.status_code)
//*[@id="arc_toolbar_report"]/div[1]/span[1]/i
