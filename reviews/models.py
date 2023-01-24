from django.db import models

from author.models import Author
from authentication.models import User

class Review(models.Model):
    title = models.CharField(verbose_name='Название отзыва', max_length=255)
    description = models.TextField(verbose_name='Содержание')
    author = models.ForeignKey(Author, verbose_name='Риелтор', on_delete=models.CASCADE, related_name='review_on')
    user = models.ForeignKey(User, verbose_name='Автор отзыва', on_delete=models.CASCADE, related_name='review_from')


    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

