# Generated by Django 4.1.5 on 2023-01-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('photo', models.ImageField(upload_to='authors', verbose_name='Фото')),
                ('bio', models.TextField(verbose_name='О себе')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
    ]
