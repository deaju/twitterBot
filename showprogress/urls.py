from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nagoyan/$', views.sakura, name='nagoyan'),
    url(r'^nagoyantest/$', views.sakuraTest, name='nagoyanTest'),
    url(r'^deaju/$', views.deaju, name='deaju'),
    url(r'dashbord/$', views.dashbord, name='dashbord'),
    url(r'^(?P<url>[\w]+)/$', views.detail, name='detail'),
]
