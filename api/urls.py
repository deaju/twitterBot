from rest_framework import routers
from .views import HistoryViewSet, NagoyanSakuraSet, HistoryFilterViewSet
from django.conf.urls import url


router = routers.DefaultRouter()
router.register(r'progress',HistoryFilterViewSet,'Progress')
router.register(r'nagoyan', NagoyanSakuraSet)

urlpatterns = patterns(url(r'^progress/(?P<title>[\w]+)/$',HistoryFilterViewSet.as_view()))