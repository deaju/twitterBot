from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from .models import History

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, title):
    latest_history_list = History.objects.filter(title=title).order_by('date')[:4]
    json_serializer = serializers.get_serializer('json')()
    json_serializer.serialize(latest_history_list,ensure_ascii=False);
    context = {'latest_history_list': latest_history_list}
    return render(request, 'graph/index20.html', context)
