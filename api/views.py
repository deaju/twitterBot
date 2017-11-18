import django_filters
from rest_framework import viewsets, filters
from .models import History,NagoyanSakura
from .serializer import HistorySerializer, NagoyanSakuraSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class NagoyanSakuraSet(viewsets.ModelViewSet):
    queryset = NagoyanSakura.objects.all()
    serializer_class = NagoyanSakuraSerializer