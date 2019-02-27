"""
开发网站的自动签到脚本，目前实现的网站有
    - 轻之国度(www.lightnovel.com)
    - 绯月论坛()
"""
from selenium import webdriver
import time

LK_cookies = r'discuz_2132_saltkey=XktjgbNo; discuz_2132_lastvisit=1537105303; UM_distinctid=165e2d4a787db-04ed564f5d97ae-9393265-100200-165e2d4a78837; discuz_2132_auth=8641SbkodL6czD7TRYErVamEIQ12flJabYrGR9nL9cthgQD2hVKi7l263OU09FNyP65xtUbAHbo%2B2oxzxO4o84%2B7YCQ; discuz_2132_lastcheckfeed=966716%7C1537108980; discuz_2132_connect_is_bind=1; discuz_2132_nofavfid=1; discuz_2132_visitedfid=194; discuz_2132_smile=5D1; discuz_2132_home_readfeed=1538342181; discuz_2132_ulastactivity=1538424033%7C0; CNZZDATA1274060484=1364711002-1537104361-%7C1538420166; discuz_2132_noticeTitle=1; discuz_2132_ignore_notice=1; discuz_2132_lastact=1538424829%09home.php%09spacecp'
KF_cookies = r'2ed4e_skinco=default; 2ed4e_ck_info=%2F%09; 2ed4e_threadlog=%2C9%2C24%2C41%2C; Hm_lvt_f83dc734066b108cb0068c6118d230ce=1550867023,1550871221; 2ed4e_winduser=DQ4LVARTPFINBwBSVQJXVwFUWgYOUVZSU1UAUgQDBwZXBFRVXgINbQ%3D%3D; 2ed4e_lastvisit=0%091550871219%09%2Findex.php%3F; 2ed4e_lastpos=index; PHPSESSID=pn43gmh30c5cna9f5pf2pu7gp0; 2ed4e_ol_offset=3686; Hm_lpvt_f83dc734066b108cb0068c6118d230ce=1550871227'


def get_cookies(original_cookies):
    cookies = dict()
    original_cookies = original_cookies.split('; ')
    for cookie in original_cookies:
        cookie = cookie.split('=')
        cookies[cookie[0]] = cookie[1]
    return cookies


class LOGIN(object):
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument('lang=zh_CN.UTF-8')
        option.add_argument(
            r'User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"'
        )
        self.driver = webdriver.Chrome(chrome_options=option,executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

    def LK_login(self):
        url = 'https://www.lightnovel.cn/forum.php'
        do_url = 'https://www.lightnovel.cn/home.php?mod=task&do=apply&id=98'
        cookies = get_cookies(LK_cookies)
        self.driver.get(url)
        for key, value in cookies.items():
            self.driver.add_cookie({'name': key, 'value': value})
        try:
            self.driver.get(do_url)
        finally:
            pass
        self.driver.delete_all_cookies()
        time.sleep(2)

    def KF_login(self):
        url = 'https://bbs.2dkf.com/index.php'
        do_url = 'https://bbs.2dkf.com/kf_growup.php?ok=3&safeid=fe593ee'
        cookies = get_cookies(KF_cookies)
        self.driver.get(url)
        for key, value in cookies.items():
            self.driver.add_cookie({'name': key, 'value': value})
        try:
            self.driver.get(do_url)
        finally:
            pass
        '''
        self.driver.find_element_by_xpath(
            '//*[@id="alldiv"]/div[4]/div[2]/div[7]/table/tbody/tr[2]/td/div/a[2]'
        ).click()
        '''
        time.sleep(3)
        self.driver.delete_all_cookies()

    def close(self):
        self.driver.close()


if __name__ == "__main__":
    auto_login = LOGIN()
    auto_login.KF_login()
    auto_login.close()
