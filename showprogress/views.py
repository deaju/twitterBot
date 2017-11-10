from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from .models import History,NagoyanSakura

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, title):
    latest_history_list = History.objects.filter(title=title).order_by('date')[:6]
    json_serializer = serializers.get_serializer('json')()
    json_serializer.serialize(latest_history_list,ensure_ascii=False)
    context = {'latest_history_list': latest_history_list}
    return render(request, 'graph/index20.html', context)

def sakura(request):
    latest_history_list = NagoyanSakura.objects.filter().order_by('date').reverse()[:6]
    context = {'progress':getProgress(latest_history_list) ,'date':getDate(latest_history_list)}
    return render(request, 'graph/index20.html', context)

def getDate(history_list):
    returnValue=[]
    for history in history_list:
        returnValue.append(history.date.strftime("%Y/%m/%d"))
    return returnValue
def getProgress(history_list):
    returnValue=[]
    for history in history_list:
        returnValue.append(history.progress)
    return returnValue