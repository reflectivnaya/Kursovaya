# Generated by Django 3.2 on 2023-01-24 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_remove_ads_type_ads'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='ads',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='ads',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название объявления'),
        ),
        migrations.AddField(
            model_name='ads',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название объявления'),
        ),
    ]
