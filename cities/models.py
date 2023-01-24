from django.db import models

class Cities(models.Model):
    city = models.CharField(verbose_name='Город', max_length=255)
  

    def __str__(self):
        return self.city

    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
