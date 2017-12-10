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

def sakura(request):
    return render(request, 'graph/index20.html')
def sakuraTest(request):
    return render(request, 'app/sakura.html')

def dashbord(request):
    animes = History.objects.values('title','url').annotate(dcount=Count('title'))
    context = {'animes':animes}
    return render(request, 'app/index.html',context)

