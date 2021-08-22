import datetime
from django.core.exceptions import ValidationError


def validate_birth_date(value):
    """
    Проверяет корректность даты рождения
    :param_value: Дата рождения (date)
    """
    if value > datetime.datetime.now().date():
        raise ValidationError('Дата не может быть больше текущей')