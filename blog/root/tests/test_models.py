import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase


class TestProfileModel(TestCase):
    
    def test_number(self):
        with self.assertRaises(ValidationError):
            user = User.objects.create(
                username='Artems', password='qwertyuiopqwe', email='artem@artem.com'
            )
        user.user_profile.city = 'asaf23'
        user.user_profile.full_clean()
        user.save()