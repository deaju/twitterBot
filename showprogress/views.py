from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from api.models import History,NagoyanSakura
from django.db.models import Count,Sum
from datetime import datetime, timedelta
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def deaju(request):
    animes = getAnimes()
    context = {'animes':animes}
    return render(request, 'graph/progressList.html',context)

def detail(request, url):
    title = History.objects.filter(url=url)[0].title
    context = {
        'title':title,
        'url': url
        }
    return render(request, 'graph/progressDetail.html', context)

def sakura(request):
    context = {
       'user':'nagoyan',
       'profile':'/static/images/anger.jpg',
       'progress':getSakuraProgress(NagoyanSakura,0),
       'yesterday':calSubSakuraProgress(NagoyanSakura,0,1),
       'lastWeek':calSubSakuraProgress(NagoyanSakura,0,7),
    }
    return render(request, 'app/sakura.html', context)

def dashbord(request):
    animes = getAnimes()
    context = {
        'user':'deaju',
        'profile':'/static/images/anger.jpg',
        'all':len(animes),
        'done':0,
        'num':calcSubAll(animes),
        'animes':animes
    }
    return render(request, 'app/index.html',context)

def dashbordDetail(request,url):
    title = History.objects.filter(url=url)[0].title
    context = {
       'user':'deaju',
       'profile':'/static/images/anger.jpg',
       'progress':getHistoryProgress(History,0,title),
       'yesterday':calSubProgress(History,0,1,title),
       'lastWeek':calSubProgress(History,0,7,title),
       'title':title,
       'url': url
    }
    return render(request, 'app/detail.html', context)

def getAnimes():
    return History.objects.values('title','url').annotate(dcount=Count('title'))

def calcSubAll(animes):
    day = getOldDate(1)
    yesterday = getOldDate(2)
    totalNum = calcSubAllDay(getOldDate(1),getOldDate(0)) - calcSubAllDay(getOldDate(2),getOldDate(1))
    return totalNum

def getOldDate(day):
    return (datetime.now() - timedelta(days=day)).strftime("%Y-%m-%d")

def calcSubAllDay(day1,day2):
    return History.objects.filter(date__gte=day1, date__lte=day2).all().aggregate(Sum('num'))['num__sum']

def getHistoryProgress(object,index,title):
    return object.objects.filter(title=title).values('date','num').order_by('-date')[index]['num']

def calSubProgress(object,index1,index2,title):
    return getHistoryProgress(object,index1,title) - getHistoryProgress(object,index2,title)

def getSakuraProgress(object,index):
    return object.objects.values('date','progress').order_by('-date')[index]['progress']

def calSubSakuraProgress(object,index1,index2):
    return getSakuraProgress(object,index1) - getSakuraProgress(object,index2)