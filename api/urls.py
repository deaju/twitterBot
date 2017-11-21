from rest_framework import routers
from .views import HistoryViewSet, NagoyanSakuraSet, HistoryFilterViewSet
from django.conf.urls import url


router = routers.DefaultRouter()
router.register(r'progress_all',HistoryFilterViewSet)
router.register(r'nagoyan', NagoyanSakuraSet)
