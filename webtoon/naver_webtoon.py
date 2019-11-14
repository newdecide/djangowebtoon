import requests

html = requests.get("https://comic.naver.com/webtoon/weekdayList.nhn?week=mon")
print("status code:", html.status_code)
print(html.text)

