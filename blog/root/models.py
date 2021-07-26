from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateField, TextField
from django.db.models.fields.files import ImageField
from django.utils import timezone


def user_avatar_path(instance, filename):
    return f'user_{instance.user.id}/avatar/{filename}'


def user_directory_path(instance, filename):
    return f'user_{instance.author.id}/photo_adverts/{filename}'


class Category(models.Model):
    """Категории объявлений"""

    category_name = models.TextField(max_length=50)
    sub_category = models.TextField(max_length=50)


class Advert(models.Model):
    """Обьявление пользователя"""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.TextField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to=user_directory_path)
    date_pub = models.DateTimeField(default=timezone.now)

class Profile(models.Model):
    """Модель пользователя"""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile'
    )
    avatar = models.ImageField(upload_to=user_avatar_path)
    birth_date = models.DateField(blank=True, null=True)
    bookmarks = models.ManyToManyField(
        Advert, related_name='users_bookmark', blank=True
    )