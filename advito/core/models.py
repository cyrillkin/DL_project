from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateField, TextField
from django.db.models.fields.files import ImageField
from django.utils import timezone


def user_avatar_path(instance, filename):
  return f'user_{instance.user.id}/avatar/{filename}'

def user_directory_path(instance, filename):
  return f'user_{instance.author.id}/posts/{filename}'


class Profile(models.Model):
  """Модель профиля для пользователя"""

  user = models.OneToOneField(
    User, on_delete=models.CASCADE, related_name='user_profile'
  )
  birth_date = models.DateField(blank=True, null=True)
  about = models.TextField(max_length=500)
  avatar = models.ImageField(upload_to=user_avatar_path)
  friends = models.ManyToManyField(
    User, blank=True, related_name='friends'
  )

class Post(models.Model):
  """Пост пользователя с картинкой"""

  author = models.ForeignKey(User, on_delete=models.CASCADE)
  description = models.TextField(max_length=1000, blank=True)
  image = models.ImageField(upload_to=user_directory_path)
  date_pub = models.DateTimeField(default=timezone.now)
  date_edit = models.DateTimeField(default=timezone.now)
  likes = models.ManyToManyField(
    User, related_name='user_like_it', blank=True
  )

class Comment(models.Model):
  """Комментарии"""
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  text = models.TextField(max_length=700)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  date_pub = models.DateTimeField(default=timezone.now)