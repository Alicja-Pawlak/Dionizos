# Generated by Django 3.1.3 on 2021-01-27 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20210126_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='wine',
            new_name='Wine',
        ),
    ]