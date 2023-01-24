from django.db import models
from author.models import Author
from authentication.models import User
from cities.models import Cities
from types_ads.models import TypesAds

class Ads(models.Model):
    title = models.CharField(verbose_name='Название объявления', max_length=255)
    author = models.ForeignKey(Author, verbose_name='Автор', on_delete=models.CASCADE, related_name='ads')
    description = models.TextField(verbose_name='Описание')
    adress = models.TextField(verbose_name='Адрес')
    photo = models.ImageField(verbose_name='Фото', upload_to='ads/photos')
    city = models.ForeignKey(Cities, verbose_name='Город', on_delete=models.CASCADE, related_name='ads')
    type = models.ForeignKey(TypesAds, verbose_name='Тип объявления', on_delete=models.CASCADE, related_name='ads')

    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

class FavouriteAdd(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    add = models.ForeignKey(Ads, verbose_name='Recipe', on_delete=models.CASCADE)

