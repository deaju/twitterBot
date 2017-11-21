from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from .models import History,NagoyanSakura
from django.db.models import Count

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def deaju(request):
    animes = History.objects.values('title').annotate(dcount=Count('title'))
    context = {'animes':animes}
    return render(request, 'graph/progressList.html',context)

def detail(request, title):
    context = {'title': title}
    return render(request, 'graph/progressDetail.html', context)    

def sakura(request):
    return render(request, 'graph/index20.html')

