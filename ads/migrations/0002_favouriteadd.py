# Generated by Django 4.1.5 on 2023-01-24 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.ads', verbose_name='Recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
