# Generated by Django 3.1.3 on 2021-01-31 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wineimage',
            name='wineimage',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
