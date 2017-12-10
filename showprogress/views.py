from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from api.models import History,NagoyanSakura
from django.db.models import Count

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def deaju(request):
    animes = History.objects.values('title','url').annotate(dcount=Count('title'))
    context = {'animes':animes}
    return render(request, 'graph/progressList.html',context)

def detail(request, url):
    title = History.objects.filter(url=url)[0].title
    context = {
        'title':title,
        'url': url
        }
    return render(request, 'graph/progressDetail.html', context)

def sakuraT(request):
    return render(request, 'graph/index20.html')

def sakura(request):
    context = {
       'user':'nagoyan',
       'profile':'/static/images/anger.jpg',
       'progress':getHistoryProgress(NagoyanSakura,0),
       'yesterday':calSubProgress(NagoyanSakura,0,1),
       'lastWeek':calSubProgress(NagoyanSakura,0,7),
    }
    return render(request, 'app/sakura.html', context)

def dashbord(request):
    animes = History.objects.values('title','url').annotate(dcount=Count('title'))
    context = {'animes':animes}
    return render(request, 'app/index.html',context)

def getHistoryProgress(object,index):
    return object.objects.values('date','progress').order_by('-date')[index]['progress']

def calSubProgress(object,index1,index2):
    return getHistoryProgress(object,index1) - getHistoryProgress(object,index2)
