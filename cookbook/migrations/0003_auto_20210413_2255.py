# Generated by Django 3.2 on 2021-04-13 20:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cookbook', '0002_auto_20210413_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodrecipe',
            old_name='dish_name',
            new_name='dish_title',
        ),
        migrations.RemoveField(
            model_name='foodrecipe',
            name='user_profiles',
        ),
        migrations.AddField(
            model_name='foodrecipe',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourites', to=settings.AUTH_USER_MODEL),
        ),
    ]
