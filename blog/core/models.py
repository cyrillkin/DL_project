from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone


# def user_avatar_path(instance, filename):
#   return f'user_{instance.user.id}/avatar/{filename}'


# class Profile(models.Model):
#   user = models.OneToOneField(
#     User, on_delete=models.CASCADE, related_name='user_profile'
#   )
#   birth_date = models.DateField(blank=True, null=True)
#   about = models.TextField(blank=True, max_lenght=500)
#   avatar = models.ImageField(upload_to=user_avatar_path)
#   friends = models.ManyToManyField(User, blank=True, related_name='friends')