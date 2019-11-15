from django.shortcuts import render
from django.http import HttpResponse
from .naver_webtoon import *
from django.views.generic import ListView
from .daum_webtoon import *

# Create your views here.
def naver_webtoon_crw(request):
    naver_webtoon()
    return HttpResponse("네이버 웹툰 크롤링 완료")

def daum_webtoon_crw(request):
    daum_webtoon()
    return HttpResponse("다음 웹툰 크롤링 완료")


class WebtoonList(ListView):
    model = WebToon
    # default object_name / 보이도록 하려면 webtoon_list로 명명
    # context_object_name = 'webtoon_list'
    paginate_by = 25

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return WebToon.objects.filter(webtoon_name__contains=query)
        else:
            return WebToon.objects.filter(site_name='네이버')


class DaumWebtoonList(ListView):
    model = WebToon
    # default object_name / 보이도록 하려면 webtoon_list로 명명
    # context_object_name = 'daum_webtoon'
    paginate_by = 25

    def get_queryset(self):
        return WebToon.objects.filter(site_name='다음')
