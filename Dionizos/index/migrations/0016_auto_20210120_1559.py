# Generated by Django 3.1.3 on 2021-01-20 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_auto_20210120_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wines',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
