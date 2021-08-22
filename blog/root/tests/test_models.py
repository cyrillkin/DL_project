import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase


# class TestProfileModel(TestCase):
    
#     def test_birth_date(self):
#         with self.assertRaises(ValidationError):
#             user = User.objects.create(
#                 username='Artem2', password='qwertyuiopqwe', email='artem@artem.com'
#             )
#         user.user_profile.birth_date = datetime.datetime.now() + datetime.timedelta(days=3)
#         user.user_profile.full_clean()
#         user.save()