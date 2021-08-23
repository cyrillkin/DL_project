from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateField, TextField
from django.db.models.fields.files import ImageField
from .validators import validate_num


def user_avatar_path(instance, filename):
    return f'user_{instance.user.id}/avatar/{filename}'


def user_directory_path(instance, filename):
    return f'user_{instance.author.id}/photo_adverts/{filename}'


class Cat(models.Model):
    """Категории объявлений"""

    name = models.TextField(max_length=50)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

class Adv(models.Model):
    """Обьявление пользователя"""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.TextField(max_length=50)
    name_cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to=user_directory_path)
    date_pub = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Prof(models.Model):
    """Модель пользователя"""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile'
    )
    avatar = models.ImageField(upload_to=user_avatar_path)
    birth_date = models.DateField(blank=True, null=True)
    city = models.TextField(blank=True, null=True, validators=[validate_num])
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
