import requests
import bs4
from .models import WebToon

# html = requests.get("https://comic.naver.com/webtoon/weekdayList.nhn?week=mon")
# print("status code:", html.status_code)
# print(html.text)

# bs_object = bs4.BeautifulSoup(html.text, "html.parser")
# print(bs_object)
# webtoon_list = bs_object.find('div' , {'class': 'list_area daily_img'})
# print(webtoon_list)
# webtoon_list_tags = webtoon_list.findAll('li')

# for webtoon_tag in webtoon_list_tags:
    # 반복문으로 제목만 가져온다.
    # 함수로 만듦(월~일 웹툰)
    # print(webtoon_tag.find('a')['title'])
    # print(webtoon_tag.find('a').find('img')['src'])
    # print(webtoon_tag.find('dd',{'class':'desc'}).text.strip())

# 함수로 만듦(월~일 웹툰)
def naver_webtoon_day(day):
    html = requests.get("https://comic.naver.com/webtoon/weekdayList.nhn?week="+day)
    bs_object = bs4.BeautifulSoup(html.text, "html.parser")
    # print(bs_object)
    webtoon_list = bs_object.find('div', {'class': 'list_area daily_img'})
    # print(webtoon_list)
    webtoon_list_tags = webtoon_list.findAll('li')

    for webtoon_tag in webtoon_list_tags:
        webtoon = WebToon()
        webtoon.site_name = "네이버"
        webtoon.webtoon_name = webtoon_tag.find('a')['title']
        webtoon.webtoon_author = webtoon_tag.find('dd',{'class':'desc'}).text.strip()
        webtoon.webtoon_img_url = webtoon_tag.find('a').find('img')['src']
        webtoon.webtoon_id = "네이버_" + webtoon_tag.find('a')['title']

        webtoon.save()

        # print(webtoon_tag.find('a')['title'])
        # print(webtoon_tag.find('a').find('img')['src'])
        # print(webtoon_tag.find('dd',{'class':'desc'}).text.strip())



# 장고실행시 실행되버리기때문에 함수로 만듦.
def naver_webtoon():
    week_list = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

    for week in week_list:
        naver_webtoon_day(week)
