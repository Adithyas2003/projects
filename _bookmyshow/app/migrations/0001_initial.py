# Generated by Django 5.1.3 on 2024-11-18 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
                ('votes', models.IntegerField()),
                ('language', models.CharField(max_length=50)),
                ('format', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=100)),
                ('certificate', models.CharField(max_length=10)),
                ('release_date', models.DateField()),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='CastMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('image_url', models.URLField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cast', to='app.movie')),
            ],
        ),
    ]
