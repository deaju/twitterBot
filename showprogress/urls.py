from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nagoyan/$', views.sakura, name='index'),
    url(r'^(?P<title>[\w]+)/$', views.detail, name='detail'),
]
