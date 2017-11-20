from rest_framework import viewsets, filters
from rest_framework import generics
from .models import History,NagoyanSakura
from .serializer import HistorySerializer, NagoyanSakuraSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class NagoyanSakuraSet(viewsets.ModelViewSet):
    queryset = NagoyanSakura.objects.all()
    serializer_class = NagoyanSakuraSerializer

class HistoryFilterViewSet(generics.ListAPIView):
    serializer_class = HistorySerializer
    def get_queryset(self):
        query_title = self.kwargs['title']
        return History.objects.filter(title__title = query_title)