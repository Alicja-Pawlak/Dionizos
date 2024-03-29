# Generated by Django 3.1.3 on 2021-01-30 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
                'ordering': ['color'],
            },
        ),
        migrations.CreateModel(
            name='Taste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taste', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name': 'taste',
                'verbose_name_plural': 'tastes',
                'ordering': ['taste'],
            },
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=32, unique=True, verbose_name='name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descriptions', models.TextField(blank=True, default='', verbose_name='opis')),
                ('pictures', models.FileField(blank=True, upload_to='')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='wines', to='index.color', verbose_name='color')),
                ('taste', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='wines', to='index.taste', verbose_name='taste')),
            ],
        ),
        migrations.CreateModel(
            name='WineImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wineimage', models.ImageField(upload_to='', verbose_name='image')),
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wine', to='index.wine')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32, null=True, verbose_name='nickname')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='description')),
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='index.wine')),
            ],
        ),
    ]
