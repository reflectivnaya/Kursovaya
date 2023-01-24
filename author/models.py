from django.db import models


class Author(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255)
    surname = models.CharField(verbose_name='Фамилия', max_length=255)
    phone = models.CharField(verbose_name='Номер телефона', max_length = 255)
    photo = models.ImageField(verbose_name='Фото', upload_to='authors')
    bio = models.TextField(verbose_name='О себе')

    def __str__(self):
        return self.phone

    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
