# Generated by Django 3.1.5 on 2021-08-09 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0008_auto_20210606_0100'),
    ]

    operations = [
        migrations.DeleteModel(
            name='History',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
