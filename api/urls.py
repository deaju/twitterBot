from rest_framework import routers
from .views import UserViewSet, EntryViewSet


router = routers.DefaultRouter()
router.register(r'history', HistoryViewSet)
router.register(r'nagoyan', NagoyanSakuraSet)