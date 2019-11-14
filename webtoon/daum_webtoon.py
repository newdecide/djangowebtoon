import requests
import time
from .models import WebToon

# 1573710662547
# 1573712343.048958

# print(time.time())

def artist_name(artists):
    return artists[0].get('name') + "/" + artists[1].get('name')


def daum_webtoon_day(day):
    json_object = requests.get("http://webtoon.daum.net/data/pc/webtoon/list_serialized/"+day+"?timeStamp="+str(time.time())).json()
    # 현재의 상태
    # print(json_object.get('result'))
    # 데이터
    # print(json_object.get('data'))
    webtoon_list = json_object.get('data')
    for webtoon in webtoon_list:
        daum_webtoon = WebToon()
        daum_webtoon.webtoon_id = "다음_" + webtoon.get('title')
        daum_webtoon.webtoon_name = webtoon.get('title')
        daum_webtoon.webtoon_author = artist_name(webtoon.get('cartoon').get('artists'))
        daum_webtoon.webtoon_img_url = webtoon.get('thumbnailImage2').get('url')
        daum_webtoon.site_name = "다음"

        daum_webtoon.save()
        # print(webtoon.get('title')) # 제목
        # print(artist_name(webtoon.get('cartoon').get('artists')))
        # print(webtoon.get('thumbnailImage2').get('url'))

def daum_webtoon():
    weeklist = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

    for week in weeklist:
        daum_webtoon_day(week)
# daum_webtoon()