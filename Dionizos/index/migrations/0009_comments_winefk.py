# Generated by Django 3.1.3 on 2021-01-19 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20210111_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='WineFK',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='index.wines'),
            preserve_default=False,
        ),
    ]
