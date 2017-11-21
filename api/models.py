from django.db import models
from django.utils.encoding import smart_str


class History(models.Model):
    title = models.CharField(max_length=200)
    progress = models.IntegerField()
    date = models.DateTimeField()
    user = models.CharField(max_length=100)
    num = models.IntegerField()
    def __str__(self):
        return smart_str('%s %s %s %s' % (self.title, self.progress, self.date, self.user))
    class Meta:
        managed = False
        db_table = 'showprogress_history'

class NagoyanSakura(models.Model):
    date = models.DateField(blank=True, null=True)
    progress = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nagoyan_sakura'

