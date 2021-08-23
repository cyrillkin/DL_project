import datetime
from django.core.exceptions import ValidationError


def validate_num(latin):
    """
    Проверяет наличие цифр
    """
    if latin.isalnum == True:
        raise ValidationError('Присутствуют цифры')