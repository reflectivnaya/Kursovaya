from django.db import models


class TypesAds(models.Model):
    type = models.CharField(verbose_name='Тип объявления', max_length=255)
  

    def __str__(self):
        return self.type

    
    class Meta:
        verbose_name = 'Тип объявления'
        verbose_name_plural = 'Типы объявления'

