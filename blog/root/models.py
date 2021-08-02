from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateField, TextField
from django.db.models.fields.files import ImageField
from django.utils import timezone


def user_avatar_path(instance, filename):
    return f'user_{instance.user.id}/avatar/{filename}'


def user_directory_path(instance, filename):
    return f'user_{instance.author.id}/photo_adverts/{filename}'


class Cat(models.Model):
    """Категории объявлений"""

    name = models.TextField(max_length=50)


class Sub_cat(models.Model):
    """Категории объявлений"""
    
    name = models.ForeignKey(Cat, on_delete=models.CASCADE)
    sub_name = models.TextField(max_length=50)


class Adv(models.Model):
    """Обьявление пользователя"""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.TextField(max_length=50)
    sub_cat = models.ForeignKey(Sub_cat, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to=user_directory_path)
    date_pub = models.DateTimeField(default=timezone.now)


class Prof(models.Model):
    """Модель пользователя"""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile'
    )
    avatar = models.ImageField(upload_to=user_avatar_path)
    birth_date = models.DateField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    bookmarks = models.ManyToManyField(
        Adv, related_name='users_bookmark', blank=True
    )