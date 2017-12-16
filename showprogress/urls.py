from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nagoyan/$', views.sakura, name='nagoyan'),
    url(r'^deaju/$', views.deaju, name='deaju'),
    url(r'^dashbord/$', views.dashbord, name='dashbord'),
    url(r'^dashbord/(?P<url>[\w]+)/$', views.dashbordDetail, name='detail'),
    url(r'^(?P<url>[\w]+)/$', views.detail, name='detail'),
]
