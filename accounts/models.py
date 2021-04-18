from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django_mysql.models import ListCharField
from django.db.models import IntegerField
from django.dispatch import receiver


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    my_favourites = ListCharField(base_field=IntegerField(), max_length=100)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MyUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.myuser.save()
