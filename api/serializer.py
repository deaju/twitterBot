from rest_framework import serializers
from .models import History,NagoyanSakura

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('title', 'progress', 'date', 'user', 'num')

class NagoyanSakuraSerializer(serializers.ModelSerializer):
     class Meta:
        model = NagoyanSakura
        fields = ('date', 'progress')
