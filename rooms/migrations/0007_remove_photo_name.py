# Generated by Django 3.0.6 on 2020-06-18 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20200618_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='name',
        ),
    ]
