from rest_framework import routers
from .views import HistoryViewSet, NagoyanSakuraSet


router = routers.DefaultRouter()
router.register(r'history', HistoryViewSet)
router.register(r'nagoyan', NagoyanSakuraSet)