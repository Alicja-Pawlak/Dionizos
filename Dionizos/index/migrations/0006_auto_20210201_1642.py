# Generated by Django 3.1.3 on 2021-02-01 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20210201_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wineimage',
            name='wineimage',
            field=models.ImageField(upload_to=''),
        ),
    ]
