from django.shortcuts import render
from django.http import HttpResponse
from .naver_webtoon import *
from django.views.generic import ListView

# Create your views here.
def naver_webtoon_crw(request):
    naver_webtoon()
    return HttpResponse("네이버 웹툰 크롤링 완료")


class WebtoonList(ListView):
    model = WebToon
