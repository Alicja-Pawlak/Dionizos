# Generated by Django 3.1.3 on 2021-01-10 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_opinion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.TextField(max_length=32, verbose_name='nickname')),
                ('description', models.TextField(blank=True, default='', verbose_name='comment')),
            ],
        ),
        migrations.DeleteModel(
            name='Opinion',
        ),
        migrations.AddField(
            model_name='wines',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='wines', to='index.comments', verbose_name='comments'),
        ),
    ]