from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nagoyan/$', views.sakura, name='nagoyan'),
    url(r'^deaju/$', views.deaju, name='deaju'),
    url(r'^(?P<url>[\w]+)/$', views.detail, name='detail'),
]
