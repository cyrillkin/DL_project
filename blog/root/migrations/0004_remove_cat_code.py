# Generated by Django 3.2.5 on 2021-07-29 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0003_sub_cat_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='code',
        ),
    ]
