# Generated by Django 3.1.3 on 2021-01-27 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20210127_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Wine',
            new_name='wine',
        ),
    ]